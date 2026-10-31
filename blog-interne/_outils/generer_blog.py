# -*- coding: utf-8 -*-
"""Générateur du blog (dentiste-paris12.com).

Commande :  python3 blog-interne/_outils/generer_blog.py

Produit :
  - blog/index.html et blog/<article>.html (les 13 articles, auteur : Dr Benjamin Darmon) ;
  - blog-interne/dossier-relecture.html (document interne, accès refusé aux visiteurs) ;
  - le bloc de planification dans .htaccess (un article reste en 404 avant sa date) ;
  - sitemap-blog.php (ne liste que les articles déjà publiés), la ligne Sitemap de robots.txt,
    la ligne Blog de llms.txt, l'entrée /blog/ de sitemap.xml ;
  - le lien « Blog » dans le pied de page de toutes les pages du site.

Règles de rédaction du site : pas de tiret cadratin, et le vocabulaire du brossage (voir les consignes du Dr Darmon).
Le script est sans danger à relancer : il remplace ce qu'il a déjà écrit.
"""
import sys, os, re, json, math, html
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from refs_blog import REFS
from articles_blog_1 import ARTICLES_1
from articles_blog_2 import ARTICLES_2
from enrichissements_blog_1 import ENRICH_1
from enrichissements_blog_2 import ENRICH_2
from photos_blog import PHOTOS

ROOT = HERE.parents[1]
VERSION = "20261005k"
SITE = "https://www.dentiste-paris12.com"
VERIF_DATE = "31 octobre 2026"   # date de vérification des sources : à mettre à jour avant chaque mise en ligne
ARTICLES = ARTICLES_1 + ARTICLES_2
BY_SLUG = {a["slug"]: a for a in ARTICLES}
ENRICH = {**ENRICH_1, **ENRICH_2}
assert set(ENRICH) == set(BY_SLUG), "enrichissements manquants ou en trop"
assert set(PHOTOS) == set(BY_SLUG), "photos manquantes ou en trop"
for _a in ARTICLES:   # les affirmations ajoutées par les enrichissements rejoignent le dossier de relecture
    _a["claims_all"] = list(_a["claims"]) + list(ENRICH[_a["slug"]].get("claims_more", []))
CATS = ["Actualité", "Gencives", "Traitement", "Santé générale", "Implants"]
MOIS = ["janvier","février","mars","avril","mai","juin","juillet","août","septembre","octobre","novembre","décembre"]
BLOG_URL = "/blog/"

def fr_date(iso):
    y, m, d = map(int, iso.split("-"))
    return ("1er" if d == 1 else str(d)) + " " + MOIS[m-1] + " " + str(y)

def typo(s):
    """Apostrophes typographiques et espaces insécables, hors balises."""
    parts = re.split(r"(<[^>]+>)", s)
    out = []
    for p in parts:
        if p.startswith("<"):
            out.append(p); continue
        p = p.replace("'", "’")
        p = re.sub(r" ([:;?!%»])", r"&nbsp;\1", p)
        p = p.replace("« ", "«&nbsp;")
        p = re.sub(r"(\d) (mm|h|grays|ans|jours|mois)\b", r"\1&nbsp;\2", p)
        out.append(p)
    return "".join(out)

def text_of(h):
    return html.unescape(re.sub(r"<[^>]+>", " ", h))

def body_words(a):
    en = ENRICH[a["slug"]]
    parts = [a["lede"]] + a["key"] + [b for _, _, b in a["sections"]] + [a["resume"]]
    parts += [b for _, _, b in en["more"]] + list(en["figs"].values())
    parts += [t + " " + d for t, d in en["gloss"]] + en["ask"] + [q + " " + r for q, r in en["faq"]]
    return len(text_of(" ".join(parts)).split())

def reading_minutes(a):
    return max(3, math.ceil(body_words(a) / 200))

def esc(s):
    return html.escape(s, quote=True)

def linkify(b):
    """Transforme « Titre d'un autre article » en lien (masqué par le script tant que l'article n'est pas publié)."""
    def rep(m):
        t = m.group(1).strip()
        for a in ARTICLES:
            if a["title"] == t:
                return f'«&nbsp;<a class="link" data-pub="{a["date"]}" href="{BLOG_URL}{a["slug"]}">{t}</a>&nbsp;»'
        return m.group(0)
    return re.sub(r"«\s*(.+?)\s*»", rep, b)

# ------------------------------------------------------------------ gabarits issus d'une page existante
def load_shell():
    s = (ROOT / "le-brossage.html").read_text(encoding="utf-8")
    header = s[s.index('<header class="site-header">'): s.index("</header>") + len("</header>")]
    footer = s[s.index('<footer class="site-footer">'): s.index("</footer>") + len("</footer>")]
    skip = '<a class="skip-link" href="#main">Aller au contenu</a>'
    return skip, header, footer

FOOT_OLD = '<li><a href="/publications-et-conferences-implants-dentaires">Enseignement et congrès</a></li>'
FOOT_NEW = FOOT_OLD + '\n          <li><a href="/blog/">Blog</a></li>'

def shell_for(prefix):
    skip, header, footer = load_shell()
    header = header.replace('src="images/', 'src="' + prefix + 'images/')
    footer = re.sub(r"<h4>(.*?)</h4>", r"<h3>\1</h3>", footer)   # ordre des titres : le pied de page vient après des h2 et h3
    if 'href="/blog/"' not in footer:
        footer = footer.replace(FOOT_OLD, FOOT_NEW)
    return skip, header, footer

def head(title, desc, canonical, prefix, robots, ld, og_type="article", image=None, image_alt="", extra_meta=""):
    image = image or f"{SITE}/images/logo-full.png"
    return f'''<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)} | Dr Benjamin Darmon</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{canonical}">
<meta name="robots" content="{robots}">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="Dr Benjamin Darmon, chirurgien-dentiste">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{canonical}">
<meta property="og:locale" content="fr_FR">
<meta property="og:image" content="{image}">
<meta property="og:image:alt" content="{esc(image_alt)}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(desc)}">
<meta name="twitter:image" content="{image}">
{extra_meta}
<link rel="icon" type="image/png" href="{prefix}images/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,500;0,9..144,600;1,9..144,500&family=IBM+Plex+Sans:wght@400;500;600&display=swap" onload="this.onload=null;this.rel='stylesheet'">
<noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,500;0,9..144,600;1,9..144,500&family=IBM+Plex+Sans:wght@400;500;600&display=swap"></noscript>
<link rel="stylesheet" href="{prefix}css/style.css?v={VERSION}">
{ld}
</head>
<body>
'''

def tail(prefix, extra=""):
    return f'''
{extra}<script src="{prefix}js/main.js?v={VERSION}"></script>
</body>
</html>
'''

def ld_json(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False) + "</script>"

# Masque, côté navigateur, les cartes et les liens des articles dont la date n'est pas encore atteinte.
# (L'accès direct à un article futur est refusé par .htaccess : ce script ne sert qu'à l'affichage.)
DATE_SCRIPT = '''<script>
(function () {
  var t = new Date();
  var today = t.getFullYear() + '-' + ('0' + (t.getMonth() + 1)).slice(-2) + '-' + ('0' + t.getDate()).slice(-2);
  document.querySelectorAll('[data-pub]').forEach(function (e) {
    if (e.getAttribute('data-pub') > today) {
      if (e.classList.contains('post-card')) { e.classList.add('is-future'); e.hidden = true; }
      else { e.replaceWith(document.createTextNode(e.textContent)); }
    }
  });
  document.querySelectorAll('.post-related').forEach(function (s) {
    if (!s.querySelector('.post-card:not(.is-future)')) { s.hidden = true; }
  });
  var grid = document.getElementById('post-grid');
  var empty = document.getElementById('blog-empty');
  if (grid && empty && !grid.querySelector('.post-card:not(.is-future)')) { empty.hidden = false; }
})();
</script>
'''

# ------------------------------------------------------------------ cartes
def card(a):
    ph = PHOTOS[a["slug"]]
    img = (f'<span class="post-card-img"><img src="img/{a["slug"]}-640.jpg" width="640" height="336" alt="{esc(ph["alt"])}" loading="lazy" decoding="async"></span>')
    return f'''<a class="post-card" href="{BLOG_URL}{a["slug"]}" data-cat="{esc(a["cat"])}" data-pub="{a["date"]}">
  {img}
  <div class="post-card-meta"><span>{fr_date(a["date"])}</span><span class="post-tag">{typo(a["cat"])}</span></div>
  <h3>{typo(a["title"])}</h3>
  <p>{typo(a["card"])}</p>
  <div class="post-card-foot">{reading_minutes(a)}&nbsp;min de lecture</div>
</a>'''

DISCLAIMER = '<p class="post-disclaimer"><strong>Information générale.</strong> Cet article s\'appuie sur des recommandations publiées. Il ne constitue ni un diagnostic, ni une prescription, ni un conseil personnalisé : seul un examen par un chirurgien-dentiste ou un médecin permet de décider de la prise en charge qui vous convient. Ne commencez et n\'arrêtez aucun traitement sur la seule foi de cet article.</p>'

# ------------------------------------------------------------------ page article
def build_article(a):
    prefix = "../"   # chemins relatifs : la page fonctionne en ligne (/blog/) et ouverte en local
    en = ENRICH[a["slug"]]
    skip, header, footer = shell_for(prefix)
    mins = reading_minutes(a)
    canonical = f"{SITE}{BLOG_URL}{a['slug']}"
    desc = en["meta"]
    assert len(desc) <= 160, (a["slug"], len(desc))
    seo_title = en["seo_title"]
    assert len(seo_title) <= 40, (a["slug"], len(seo_title))
    ph = PHOTOS[a["slug"]]
    image = f"{SITE}/blog/img/{a['slug']}-1200.jpg"
    cites = [html.unescape(re.sub(r"<[^>]+>", "", REFS[k][0])) for k in a["refs"]]
    words = body_words(a)
    graph = [{
        "@context": "https://schema.org", "@type": "Article",
        "headline": a["title"], "description": desc,
        "datePublished": a["date"], "dateModified": a["date"], "inLanguage": "fr-FR",
        "articleSection": a["cat"], "wordCount": words, "isAccessibleForFree": True,
        "image": image,
        "author": {"@type": "Person", "name": "Dr Benjamin Darmon", "jobTitle": "Chirurgien-dentiste"},
        "publisher": {"@type": "Organization", "name": "Cabinet dentaire du Dr Benjamin Darmon", "url": SITE + "/"},
        "mainEntityOfPage": {"@type": "WebPage", "@id": canonical},
        "citation": cites,
    }, {
        "@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q,
                        "acceptedAnswer": {"@type": "Answer", "text": text_of(r).strip()}} for q, r in en["faq"]],
    }, {
        "@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Accueil", "item": SITE + "/"},
            {"@type": "ListItem", "position": 2, "name": "Blog", "item": SITE + BLOG_URL},
            {"@type": "ListItem", "position": 3, "name": a["title"]}]}]
    ld = "\n".join(ld_json(g) for g in graph)
    extra = (f'<meta name="author" content="Dr Benjamin Darmon">\n'
             f'<meta property="article:published_time" content="{a["date"]}">\n'
             f'<meta property="article:modified_time" content="{a["date"]}">\n'
             f'<meta property="article:section" content="{esc(a["cat"])}">')
    out = [head(seo_title, desc, canonical, prefix, "index, follow, max-image-preview:large", ld,
                image=image, image_alt=ph["alt"], extra_meta=extra), skip, "\n", header, '\n<main id="main">\n']
    out.append(f'''<section class="page-hero post-hero">
  <div class="wrap">
    <p class="breadcrumb"><a href="/">Accueil</a> &rsaquo; <a href="{BLOG_URL}">Blog</a> &rsaquo; <span>{typo(a["cat"])}</span></p>
    <h1>{typo(a["title"])}</h1>
    <p class="lede">{typo(a["lede"])}</p>
    <p class="post-meta"><span class="post-tag">{typo(a["cat"])}</span><span>Publié le {fr_date(a["date"])}</span><span>{mins}&nbsp;min de lecture</span><span>Sources vérifiées le {VERIF_DATE}</span></p>
  </div>
</section>
''')
    figs = dict(en["figs"])
    ids = {sid for sid, _, _ in a["sections"]} | {sid for sid, _, _ in en["more"]} | {"_intro"}
    assert set(figs) <= ids, (a["slug"], set(figs) - ids)
    toc_items = [(sid, t) for sid, t, _ in a["sections"]] + [(sid, t) for sid, t, _ in en["more"]]
    toc_items += [("glossaire", "Les mots à connaître"), ("questions", "Questions à poser à votre praticien"),
                  ("faq", "Questions fréquentes"), ("resume", "En résumé"), ("references", "Références")]
    toc = "\n".join(f'<li><a href="#{sid}">{typo(t)}</a></li>' for sid, t in toc_items)
    cover = (f'<figure class="post-cover"><img src="img/{a["slug"]}-1200.jpg" srcset="img/{a["slug"]}-640.jpg 640w, img/{a["slug"]}-1200.jpg 1200w" '
             f'sizes="(max-width: 860px) 100vw, 780px" width="1200" height="630" alt="{esc(ph["alt"])}" fetchpriority="high" decoding="async">'
             f'<figcaption>{ph["origine"]}. Elle ne montre pas un cas réel.</figcaption></figure>')
    body = [cover, typo(DISCLAIMER), '<div class="post-key"><h2>L\'essentiel</h2><ul>' + "".join(f"<li>{typo(k)}</li>" for k in a["key"]) + "</ul></div>"]
    if "_intro" in figs:
        body.append(typo(linkify(figs["_intro"])))
    for sid, t, b in list(a["sections"]) + list(en["more"]):
        body.append(f'<h2 id="{sid}">{typo(t)}</h2>\n{typo(linkify(b))}')
        if sid in figs:
            body.append(typo(linkify(figs[sid])))
    gl = "".join(f"<dt>{typo(t)}</dt><dd>{typo(d)}</dd>" for t, d in en["gloss"])
    body.append(f'<h2 id="glossaire">Les mots à connaître</h2>\n<dl class="gloss">{gl}</dl>')
    ask = "".join(f"<li>{typo(q)}</li>" for q in en["ask"])
    body.append(f'<h2 id="questions">Questions à poser à votre praticien</h2>\n<p>Ces questions peuvent vous aider à préparer un rendez-vous. Les réponses dépendent de votre situation.</p>\n<ul class="check-list ask-list">{ask}</ul>')
    faq = "".join(f'<h3 class="faq-q">{typo(q)}</h3>\n<p class="faq-a">{typo(linkify(r))}</p>' for q, r in en["faq"])
    body.append(f'<h2 id="faq">Questions fréquentes</h2>\n{faq}')
    body.append(f'<h2 id="resume">En résumé</h2>\n<p>{typo(a["resume"])}</p>')
    refs_html = "".join(f'<li>{typo(REFS[k][0])} <a href="{REFS[k][1]}" rel="noopener" target="_blank">{esc(REFS[k][1])}</a></li>' for k in a["refs"])
    body.append(f'<h2 id="references">Références</h2>\n<ol class="post-refs">{refs_html}</ol>')
    body.append(typo(f'''<aside class="post-review" aria-labelledby="auteur-title">
<h2 id="auteur-title">À propos de cet article</h2>
<dl>
<dt>Auteur</dt><dd>Dr Benjamin Darmon, chirurgien-dentiste</dd>
<dt>Publié le</dt><dd>{fr_date(a["date"])}</dd>
<dt>Sources vérifiées le</dt><dd>{VERIF_DATE}</dd>
</dl>
<p>Article d'information publié sous la responsabilité du Dr Benjamin Darmon, chirurgien-dentiste. Il est rédigé à partir de recommandations de la Haute Autorité de santé et de sociétés savantes, citées dans les références. Les recommandations évoluent : la version en vigueur est celle publiée par l'organisme cité.</p>
</aside>'''))
    body.append(typo('<p class="post-contact">Pour une question sur votre situation personnelle, un examen est nécessaire : coordonnées et prise de rendez-vous sur la page <a class="link" href="/contact">Contact</a>. N\'envoyez pas d\'informations de santé par le formulaire en ligne.</p>'))
    out.append(f'''<section>
  <div class="wrap">
    <div class="post-layout">
      <nav class="post-toc" aria-label="Sommaire">
        <p class="post-toc-title"><span>Sommaire</span><span>{mins}&nbsp;min</span></p>
        <ol>
{toc}
        </ol>
      </nav>
      <article class="post-body">
{chr(10).join(body)}
      </article>
    </div>
  </div>
</section>
''')
    rel = "\n".join(card(BY_SLUG[s]) for s in a["related"])
    out.append(f'''<section class="tint post-related">
  <div class="wrap">
    <span class="eyebrow">À lire également</span>
    <div class="post-grid">
{rel}
    </div>
  </div>
</section>
</main>
''')
    out.append(footer)
    out.append(tail(prefix, DATE_SCRIPT))
    return "".join(out)

# ------------------------------------------------------------------ accueil du blog
def build_index():
    prefix = "../"   # chemins relatifs : la page fonctionne en ligne (/blog/) et ouverte en local
    skip, header, footer = shell_for(prefix)
    title = "Blog parodontologie et implantologie"
    desc = "Articles pour les patients sur les maladies des gencives et les implants dentaires, d'après les recommandations de la HAS et de sociétés savantes."
    ld = ld_json({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Accueil", "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": "Blog"}]})
    h = head(title, desc, SITE + BLOG_URL, prefix, "index, follow, max-image-preview:large", ld, og_type="website")
    filters = '<li><button type="button" data-filter="all" aria-pressed="true">Tous</button></li>' + "".join(
        f'<li><button type="button" data-filter="{esc(c)}" aria-pressed="false">{typo(c)}</button></li>' for c in CATS)
    cards = "\n".join(card(a) for a in sorted(ARTICLES, key=lambda x: x["date"], reverse=True))
    filter_js = '''<script>
(function () {
  var buttons = document.querySelectorAll('.blog-filters button');
  var cards = document.querySelectorAll('.post-card');
  buttons.forEach(function (b) {
    b.addEventListener('click', function () {
      var f = b.getAttribute('data-filter');
      buttons.forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
      cards.forEach(function (c) { c.hidden = c.classList.contains('is-future') || !(f === 'all' || c.getAttribute('data-cat') === f); });
    });
  });
})();
</script>
'''
    page = [h, skip, "\n", header, '\n<main id="main">\n', f'''<section class="page-hero post-hero">
  <div class="wrap">
    <p class="breadcrumb"><a href="/">Accueil</a> &rsaquo; <span>Blog</span></p>
    <h1>Blog : parodontologie et implantologie</h1>
    <p class="lede">Des articles d'information pour les patients sur les maladies des gencives et les implants dentaires. Chaque article s'appuie sur des recommandations de la Haute Autorité de santé et de sociétés savantes, citées en fin de page.</p>
  </div>
</section>
<section>
  <div class="wrap">
    <p class="blog-intro">Ces articles informent : ils ne remplacent pas une consultation. Une question sur votre situation personnelle relève d'un examen. Un nouvel article est publié chaque semaine.</p>
    <p class="blog-intro" id="blog-empty" hidden>Les premiers articles seront publiés prochainement.</p>
    <ul class="blog-filters" aria-label="Filtrer par thème">{filters}</ul>
    <h2 class="sr-only">Les articles</h2>
    <div class="post-grid" id="post-grid">
{cards}
    </div>
  </div>
</section>
</main>
''', footer, tail(prefix, DATE_SCRIPT + filter_js)]
    return typo_blocks("".join(page))

def typo_blocks(s):
    return s

# ------------------------------------------------------------------ dossier de relecture interne
RULES = [
 ("Communication « par tout moyen », y compris site internet ou blog, de façon loyale, honnête et non trompeuse ; pas de témoignage de tiers, pas de comparaison avec d'autres praticiens ou établissements, pas d'incitation à un recours inutile à des soins.", "R.4127-215-1-I"),
 ("La profession ne doit pas être exercée comme un commerce.", "R.4127-215"),
 ("Informations scientifiques : n'exposer que des données scientifiquement étayées, avec prudence et mesure ; ne pas présenter comme acquise une hypothèse non confirmée ; ne pas divulguer au grand public un procédé dont la valeur et l'innocuité ne sont pas démontrées.", "R.4127-215-1-II et R.4127-226"),
 ("Ne pas tirer profit de l'information diffusée dans son activité professionnelle ni en faire bénéficier le cabinet : aucun renvoi des articles vers les pages de soins ou de tarifs du cabinet, aucun argument promotionnel.", "R.4127-215-3"),
 ("Aucune publicité pour un tiers ou une entreprise commerciale : pas de marque, pas de produit, pas de lien vers une société commerciale ; prudence avec les sociétés savantes soutenues par des industriels.", "R.4127-225"),
 ("Pas de notation, pas de photo avant/après (recommandations ordinales : risque de suggérer un résultat positif certain).", "Recommandations ordinales (version du 19/06/2026)"),
 ("Titres et orientation de pratique : n'utiliser que des titres reconnus par l'Ordre ; pas de « expert » ni de « spécialiste » sans titre.", "R.4127-220, recommandations ordinales (version du 19/06/2026)"),
 ("Pas de référencement prioritaire obtenu par un moyen payant ou non ; pas de mots-clés locaux dans les titres des articles.", "R.4127-217-II"),
 ("Pas de patient identifiable (images, radiographies, captures d'écran).", "R.4127-206 et suivants"),
 ("Confraternité : aucun article ne critique, même implicitement, les pratiques d'autres praticiens.", "R.4127-259 et R.4127-261"),
]

def build_dossier():
    prefix = "../"
    skip, header, footer = shell_for(prefix)
    h = head("Dossier de relecture du blog", "Document interne : sources, vérifications et revue des articles.", SITE + "/blog-interne/dossier-relecture", prefix, "noindex, nofollow", "")
    p = [h, skip, "\n", header, '\n<main id="main">\n']
    p.append('<div class="draft-banner"><div class="wrap">Document interne. Accès refusé aux visiteurs du site.</div></div>\n')
    p.append('''<section class="page-hero"><div class="wrap">
<p class="breadcrumb"><span>Blog (document interne)</span></p>
<h1>Dossier de relecture du blog</h1>
<p class="lede">Ce dossier relie chaque affirmation importante des 13 articles à sa source, et conserve la revue critique réalisée avant la mise en ligne.</p>
</div></section>
<section><div class="wrap measure-wide">
<h2>1. Statut de ces vérifications</h2>
<p>Les articles ont été rédigés par Claude (IA) à partir des sources listées plus bas. Ils sont publiés sous le nom du Dr Benjamin Darmon, qui en assume la responsabilité. Avant la mise en ligne, ils ont fait l'objet d'une revue critique par deux agents IA qui jouent un rôle : un responsable scientifique et un membre de l'Ordre. Ces revues sont une simulation de travail. Elles ne sont ni des validations réelles ni des avis de l'Ordre, et les articles ne s'en prévalent nulle part.</p>
<h2>2. Calendrier de publication (un article par semaine)</h2>
<p>Chaque article reste en erreur 404 avant sa date (règle écrite dans le fichier .htaccess) et n'apparaît dans le plan du site qu'à partir de cette date.</p>
<table class="dossier-table"><thead><tr><th>Publication</th><th>Thème</th><th>Article</th></tr></thead><tbody>
''')
    for a in sorted(ARTICLES, key=lambda x: x["date"]):
        p.append(f'<tr><td>{fr_date(a["date"])}</td><td>{typo(a["cat"])}</td><td>{typo(a["title"])}</td></tr>\n')
    p.append('</tbody></table>\n<h2>3. Règles de communication contrôlées</h2>\n')
    p.append('<p>Sources : code de déontologie (articles R.4127-203 et suivants du code de la santé publique, tels que repris par l\'Ordre) et recommandations ordinales en vigueur (version du 19 juin 2026, qui reprennent celles du 6 mai 2021 et le décret n° 2020-1658 du 22 décembre 2020). Légifrance n\'a pas pu être consulté : certains articles du code sont cités d\'après la compilation de l\'Ordre de mai 2024.</p>\n<table class="dossier-table"><thead><tr><th>Règle</th><th>Référence citée</th></tr></thead><tbody>\n')
    for r, ref in RULES:
        p.append(f"<tr><td>{typo(r)}</td><td>{ref}</td></tr>\n")
    p.append("</tbody></table>\n")
    frag = HERE / "rapports_agents.html"
    if frag.exists():
        p.append(frag.read_text(encoding="utf-8"))
    p.append('<h2>Affirmations et sources, article par article</h2>\n')
    for i, a in enumerate(sorted(ARTICLES, key=lambda x: x["date"]), 1):
        p.append(f'<h3 id="a{i}">{i}. {typo(a["title"])}</h3>\n<p>Publication prévue le {fr_date(a["date"])}</p>\n')
        p.append('<table class="dossier-table"><thead><tr><th>Affirmation</th><th>Source</th><th>Où la vérifier</th></tr></thead><tbody>\n')
        for claim, key, loc in a["claims_all"]:
            p.append(f'<tr><td>{typo(claim)}</td><td>{typo(REFS[key][0])}</td><td>{typo(loc)}</td></tr>\n')
        p.append("</tbody></table>\n")
    p.append('<h2>Illustrations des articles</h2>\n<p>Images générées par intelligence artificielle (ChatGPT) à partir de prompts rédigés pour la charte graphique du site, puis recadrées (1200 x 630 et 640 x 336). Aucun patient identifiable, aucun avant/après, aucune marque ni texte lisible. <strong>À valider par le Dr Darmon :</strong> une image générée peut comporter des inexactitudes anatomiques (nombre de racines, forme de l\'implant, niveau de l\'os). La légende sous chaque image précise qu\'elle est générée par intelligence artificielle et qu\'elle ne montre pas un cas réel.</p>\n<table class="dossier-table"><thead><tr><th>Article</th><th>Texte alternatif</th><th>Remarque</th></tr></thead><tbody>\n')
    for a in sorted(ARTICLES, key=lambda x: x["date"]):
        ph = PHOTOS[a["slug"]]
        p.append(f'<tr><td>{typo(a["title"])}</td><td>{typo(ph["alt"])}</td><td>{typo(ph["note"])}</td></tr>\n')
    p.append("</tbody></table>\n")
    p.append('<h2>Bibliographie complète et état de la vérification</h2>\n<table class="dossier-table"><thead><tr><th>Référence</th><th>Lien</th><th>Statut</th></tr></thead><tbody>\n')
    for k, (cit, url, st) in REFS.items():
        cls = ' class="dossier-flag"' if st.startswith("A CONFIRMER") else ""
        p.append(f'<tr><td>{typo(cit)}</td><td><a href="{url}" rel="noopener" target="_blank">{esc(url)}</a></td><td{cls}>{esc(st)}</td></tr>\n')
    p.append("</tbody></table>\n</div></section>\n</main>\n")
    p += [footer, tail(prefix)]
    return "".join(p)

# ------------------------------------------------------------------ intégration au site
HT_BEGIN = "# BLOG-PLANNING-DEBUT (genere par blog-interne/_outils/generer_blog.py, ne pas modifier a la main)"
HT_END = "# BLOG-PLANNING-FIN"

def htaccess_block():
    lines = [HT_BEGIN,
             "# Un article du blog renvoie une erreur 404 tant que sa date de publication n'est pas atteinte (heure du serveur).",
             "# Il suffit de deposer le site : aucune action manuelle n'est necessaire."]
    for a in sorted(ARTICLES, key=lambda x: x["date"]):
        stamp = a["date"].replace("-", "") + "000000"
        lines.append(f"RewriteCond %{{TIME}} <{stamp}")
        lines.append(f"RewriteRule ^blog/{a['slug']}(\\.html)?$ - [R=404,L]")
    lines.append(HT_END)
    return "\n".join(lines) + "\n"

def update_htaccess():
    p = ROOT / ".htaccess"
    t = p.read_text(encoding="utf-8")
    t = re.sub(re.escape(HT_BEGIN) + r".*?" + re.escape(HT_END) + r"\n?", "", t, flags=re.S)
    anchor = "# --- Anciennes fiches PDF"
    assert anchor in t, "ancre .htaccess introuvable"
    t = t.replace(anchor, htaccess_block() + "\n" + anchor, 1)
    p.write_text(t, encoding="utf-8")

def write_sitemap_php():
    items = ",\n".join(f"  ['slug' => '{a['slug']}', 'date' => '{a['date']}']" for a in sorted(ARTICLES, key=lambda x: x["date"]))
    code = f'''<?php
// Plan du site du blog : ne liste que les articles dont la date de publication est atteinte.
// Genere par blog-interne/_outils/generer_blog.py. Reference dans robots.txt.
header('Content-Type: application/xml; charset=utf-8');
date_default_timezone_set('Europe/Paris');
$today = date('Y-m-d');
$articles = [
{items}
];
echo '<?xml version="1.0" encoding="UTF-8"?>' . "\\n";
echo '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' . "\\n";
foreach ($articles as $a) {{
    if ($a['date'] <= $today) {{
        echo '  <url><loc>{SITE}/blog/' . $a['slug'] . '</loc><lastmod>' . $a['date'] . '</lastmod><changefreq>monthly</changefreq><priority>0.5</priority></url>' . "\\n";
    }}
}}
echo '</urlset>' . "\\n";
'''
    (ROOT / "sitemap-blog.php").write_text(code, encoding="utf-8")

def update_site_files():
    # robots.txt
    rp = ROOT / "robots.txt"
    t = rp.read_text(encoding="utf-8")
    line = f"Sitemap: {SITE}/sitemap-blog.php"
    if line not in t:
        t = t.rstrip("\n") + "\n" + line + "\n"
    rp.write_text(t, encoding="utf-8")
    # sitemap.xml : l'accueil du blog
    sp = ROOT / "sitemap.xml"
    t = sp.read_text(encoding="utf-8")
    loc = f"{SITE}{BLOG_URL}"
    if loc not in t:
        t = t.replace("</urlset>", f"  <url><loc>{loc}</loc><lastmod>2026-10-31</lastmod><changefreq>weekly</changefreq><priority>0.6</priority></url>\n</urlset>")
    sp.write_text(t, encoding="utf-8")
    # llms.txt
    lp = ROOT / "llms.txt"
    t = lp.read_text(encoding="utf-8")
    line = f"- Blog parodontologie et implantologie (un article par semaine, sources citées) : {SITE}{BLOG_URL}"
    if line not in t:
        t = t.rstrip("\n") + "\n" + line + "\n"
    lp.write_text(t, encoding="utf-8")
    # pied de page de toutes les pages
    for f in ROOT.glob("*.html"):
        t = f.read_text(encoding="utf-8")
        if FOOT_OLD in t and 'href="/blog/"' not in t:
            f.write_text(t.replace(FOOT_OLD, FOOT_NEW), encoding="utf-8")

def main():
    blog = ROOT / "blog"
    blog.mkdir(exist_ok=True)
    for a in ARTICLES:
        (blog / (a["slug"] + ".html")).write_text(build_article(a), encoding="utf-8")
    (blog / "index.html").write_text(build_index(), encoding="utf-8")
    (ROOT / "blog-interne" / "dossier-relecture.html").write_text(build_dossier(), encoding="utf-8")
    update_htaccess()
    write_sitemap_php()
    update_site_files()
    print(len(ARTICLES), "articles générés dans", blog)

if __name__ == "__main__":
    main()
