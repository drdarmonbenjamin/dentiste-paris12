# -*- coding: utf-8 -*-
"""Composants visuels du blog : schémas SVG originaux et graphiques en HTML/CSS.

Les graphiques sont en HTML (texte réel, lisible par les moteurs de recherche et les lecteurs d'écran,
adaptable au mobile). Les schémas anatomiques sont de simples illustrations originales, sans texte intégré :
les légendes sont écrites en HTML sous chaque schéma. Aucune donnée n'est inventée : chaque chiffre
affiché vient d'une source citée dans l'article.
"""
import html as _h

def _e(s):
    return _h.escape(s, quote=True)

# ------------------------------------------------------------------ cadre commun
def figure(inner, caption, cls="", label=None):
    lab = f' aria-label="{_e(label)}"' if label else ""
    return f'<figure class="fig {cls}"{lab}>{inner}<figcaption>{caption}</figcaption></figure>'

# ------------------------------------------------------------------ étapes (flux)
def flow(steps, caption, label="Étapes"):
    """steps : liste de (titre, texte)."""
    lis = "".join(
        f'<li><span class="flow-n" aria-hidden="true">{i}</span><div><strong>{t}</strong><p>{p}</p></div></li>'
        for i, (t, p) in enumerate(steps, 1))
    return figure(f'<ol class="flow">{lis}</ol>', caption, "fig-flow", label)

def loop(steps, caption, label="Cycle"):
    lis = "".join(f'<li><strong>{t}</strong><p>{p}</p></li>' for t, p in steps)
    return figure(f'<ol class="loop">{lis}</ol><p class="loop-back" aria-hidden="true">Le cycle se poursuit</p>', caption, "fig-loop", label)

# ------------------------------------------------------------------ tableau de verdicts
CHIPS = {
    "oui": ('chip chip-yes', 'Recommandé'),
    "non": ('chip chip-no', 'Non recommandé'),
    "cas": ('chip chip-case', 'Selon la situation'),
    "sug": ('chip chip-sug', 'Suggéré'),
    "nsug": ('chip chip-no', 'Non suggéré'),
    "ouv": ('chip chip-case', 'Laissé au praticien'),
    "assoc": ('chip chip-case', 'Associé à un risque accru'),
    "moins": ('chip chip-sug', 'Données moins tranchées'),
    "inc": ('chip chip-no', 'On ne sait pas encore'),
}

def verdict_table(rows, caption, head=("Situation", "Position"), label="Tableau récapitulatif"):
    """rows : liste de (libellé, clé de CHIPS, précision facultative)."""
    body = ""
    for lab, key, note in rows:
        cls, txt = CHIPS[key]
        n = f'<span class="vt-note">{note}</span>' if note else ""
        body += f'<tr><th scope="row">{lab}</th><td><span class="{cls}">{txt}</span>{n}</td></tr>'
    t = (f'<table class="verdict"><thead><tr><th scope="col">{head[0]}</th><th scope="col">{head[1]}</th></tr></thead>'
         f'<tbody>{body}</tbody></table>')
    return figure(t, caption, "fig-table", label)

# ------------------------------------------------------------------ graphique à intervalles (axe visible)
def interval_plot(rows, lo, hi, step, unit, caption, label="Graphique"):
    """rows : liste de dict(label, est, ci=(a,b), pred=(c,d) ou None, note). Axe de lo à hi, affiché."""
    span = float(hi - lo)
    def pos(v):
        return max(0.0, min(100.0, (v - lo) / span * 100.0))
    ticks = ""
    v = lo
    while v <= hi + 1e-9:
        ticks += f'<span class="ip-tick" style="left:{pos(v):.2f}%">{("%g" % v).replace(".", ",")}{unit}</span>'
        v += step
    out = ""
    for r in rows:
        a, b = r["ci"]
        pred = ""
        if r.get("pred"):
            c, d = r["pred"]
            pred = f'<span class="ip-pred" style="left:{pos(c):.2f}%;width:{pos(d)-pos(c):.2f}%"></span>'
        txt = f'{r["est"]:g}{unit}'.replace(".", ",")
        ci_txt = f'intervalle de confiance à 95 % : de {str(a).replace(".", ",")} à {str(b).replace(".", ",")}{unit}'
        pr_txt = ""
        if r.get("pred"):
            pr_txt = f' ; intervalle de prédiction : de {str(r["pred"][0]).replace(".", ",")} à {str(r["pred"][1]).replace(".", ",")}{unit}'
        out += (f'<div class="ip-row"><div class="ip-label">{r["label"]}<span class="ip-val">{txt}</span></div>'
                f'<div class="ip-track" role="img" aria-label="{_e(r["label"])} : {_e(txt)} ; {_e(ci_txt)}{_e(pr_txt)}">'
                f'{pred}<span class="ip-ci" style="left:{pos(a):.2f}%;width:{pos(b)-pos(a):.2f}%"></span>'
                f'<span class="ip-dot" style="left:{pos(r["est"]):.2f}%"></span></div>'
                f'<div class="ip-note">{ci_txt.capitalize()}{pr_txt}.</div></div>')
    inner = f'<div class="ip">{out}<div class="ip-axis" aria-hidden="true">{ticks}</div></div>'
    return figure(inner, caption, "fig-ip", label)

# ------------------------------------------------------------------ barres simples (axe de zéro à max)
def bars(rows, vmax, unit, caption, label="Graphique en barres"):
    """rows : liste de (libellé, valeur, précision)."""
    out = ""
    for lab, val, note in rows:
        w = max(1.0, min(100.0, val / float(vmax) * 100.0))
        txt = f'{val:g}{unit}'.replace(".", ",")
        n = f'<span class="br-note">{note}</span>' if note else ""
        out += (f'<div class="br-row"><div class="br-label">{lab}</div>'
                f'<div class="br-track" role="img" aria-label="{_e(lab)} : {_e(txt)}"><span class="br-bar" style="width:{w:.2f}%"></span></div>'
                f'<div class="br-val">{txt}{n}</div></div>')
    return figure(f'<div class="br">{out}</div>', caption, "fig-bars", label)

# ------------------------------------------------------------------ échelle segmentée
def scale(segments, caption, label="Échelle"):
    """segments : liste de (valeur affichée, libellé, intensité 0 à 3)."""
    out = "".join(f'<li class="sc-{lv}"><strong>{v}</strong><span>{t}</span></li>' for v, t, lv in segments)
    return figure(f'<ol class="scale">{out}</ol>', caption, "fig-scale", label)

# ------------------------------------------------------------------ pictogramme (n sur 10)
def pictogram(n, total, caption, label="Pictogramme"):
    dots = "".join(f'<span class="dot{" on" if i < n else ""}"></span>' for i in range(total))
    return figure(f'<div class="picto" role="img" aria-label="{_e(label)} : {n} sur {total}">{dots}</div>', caption, "fig-picto", label)

# ------------------------------------------------------------------ cartes de comparaison
def cards(items, caption, label="Comparaison"):
    """items : liste de (titre, texte)."""
    out = "".join(f'<div class="cmp"><strong>{t}</strong><p>{p}</p></div>' for t, p in items)
    return figure(f'<div class="cmp-grid">{out}</div>', caption, "fig-cards", label)

def bidirectional(a, b, caption, label="Lien dans les deux sens"):
    inner = (f'<div class="bidi"><div class="bidi-box">{a}</div>'
             f'<div class="bidi-arrows" aria-hidden="true"><span>&rarr;</span><span>&larr;</span></div>'
             f'<div class="bidi-box">{b}</div></div>')
    return figure(inner, caption, "fig-bidi", label)

# ------------------------------------------------------------------ schémas anatomiques (SVG sans texte)
GUM = {"sain": "#F2B8B5", "rouge": "#E27D7D"}
BONE = "#E9D9B8"
LINE = "#6F8293"

def _tooth_state(kind):
    """kind : 'sain', 'gingivite', 'parodontite'."""
    if kind == "sain":
        gm, bone, gum_c, plaque, calc, bulge = 98, 122, GUM["sain"], False, False, 0
    elif kind == "gingivite":
        gm, bone, gum_c, plaque, calc, bulge = 94, 122, GUM["rouge"], True, False, 7
    else:
        gm, bone, gum_c, plaque, calc, bulge = 126, 166, GUM["rouge"], True, True, 0
    tooth = ('M70,42 Q70,16 100,16 Q130,16 130,42 L130,100 Q128,152 110,202 Q100,216 90,202 Q72,152 70,100 Z')
    left = (f'M0,{gm+8} Q38,{gm-4-bulge} 69,{gm} L69,{bone+12} L0,{bone+6} Z')
    right = (f'M200,{gm+8} Q162,{gm-4-bulge} 131,{gm} L131,{bone+12} L200,{bone+6} Z')
    bone_l = f'M0,{bone+6} L69,{bone+12} L69,250 L0,250 Z'
    bone_r = f'M200,{bone+6} L131,{bone+12} L131,250 L200,250 Z'
    extra = ""
    if kind == "parodontite":
        # poche : espace sombre entre la dent et la gencive, jusqu'à la crête osseuse
        extra += (f'<path d="M69,{gm} L69,{bone+12} L76,{bone+12} L76,{gm+4} Z" fill="#8C5A5A" opacity=".55"/>'
                  f'<path d="M131,{gm} L131,{bone+12} L124,{bone+12} L124,{gm+4} Z" fill="#8C5A5A" opacity=".55"/>')
    if plaque:
        extra += ''.join(f'<circle cx="{x}" cy="{y}" r="3.2" fill="#E8D27A"/>' for x, y in
                         [(66, gm-4), (134, gm-4), (68, gm+6), (132, gm+6), (73, gm-10), (127, gm-10)])
    if calc:
        extra += ''.join(f'<rect x="{x}" y="{y}" width="6" height="9" rx="2" fill="#B59A5B"/>' for x, y in
                         [(64, gm+16), (130, gm+22), (64, gm+34), (130, gm+40)])
    if kind == "gingivite":
        extra += ''.join(f'<path d="M{x},{y} q-3,5 0,8 q3,-3 0,-8z" fill="#B0262F"/>' for x, y in [(83, gm+14), (117, gm+16)])
    return (f'<svg viewBox="0 0 200 250" role="img" aria-hidden="true" focusable="false">'
            f'<path d="{bone_l}" fill="{BONE}"/><path d="{bone_r}" fill="{BONE}"/>'
            f'<path d="{left}" fill="{gum_c}"/><path d="{right}" fill="{gum_c}"/>'
            f'<path d="{tooth}" fill="#fff" stroke="{LINE}" stroke-width="2.5"/>{extra}</svg>')

def tooth_triptych(items, caption, label="Schémas de la gencive"):
    """items : liste de (kind, légende courte HTML). kind dans sain, gingivite, parodontite."""
    out = "".join(f'<figure class="tri"><div class="tri-art">{_tooth_state(k)}</div><figcaption>{t}</figcaption></figure>' for k, t in items)
    legend = ('<p class="tri-legend"><span class="lg lg-gum"></span>Gencive '
              '<span class="lg lg-bone"></span>Os '
              '<span class="lg lg-plaque"></span>Plaque '
              '<span class="lg lg-calc"></span>Tartre</p>')
    two = " tri-two" if len(items) == 2 else ""
    return figure(f'<div class="tri-grid{two}">{out}</div>{legend}', caption, "fig-tri", label)

def _implant_state(kind):
    """kind : 'sain', 'mucosite', 'perimplantite'."""
    if kind == "sain":
        gm, bone, gum_c = 92, 112, GUM["sain"]
    elif kind == "mucosite":
        gm, bone, gum_c = 88, 112, GUM["rouge"]
    else:
        gm, bone, gum_c = 108, 150, GUM["rouge"]
    imp_top = 96
    threads = "".join(f'<line x1="86" y1="{y}" x2="114" y2="{y+5}" stroke="#9AA8B3" stroke-width="2"/>' for y in range(imp_top+6, 214, 12))
    left = f'M0,{gm+8} Q38,{gm-4} 83,{gm} L83,{bone+10} L0,{bone+6} Z'
    right = f'M200,{gm+8} Q162,{gm-4} 117,{gm} L117,{bone+10} L200,{bone+6} Z'
    bone_l = f'M0,{bone+6} L83,{bone+10} L83,250 L0,250 Z'
    bone_r = f'M200,{bone+6} L117,{bone+10} L117,250 L200,250 Z'
    extra = ""
    if kind == "perimplantite":
        extra = (f'<path d="M83,{gm} L83,{bone+10} L90,{bone+10} L90,{gm+4} Z" fill="#8C5A5A" opacity=".55"/>'
                 f'<path d="M117,{gm} L117,{bone+10} L110,{bone+10} L110,{gm+4} Z" fill="#8C5A5A" opacity=".55"/>')
    if kind != "sain":
        extra += ''.join(f'<circle cx="{x}" cy="{y}" r="3.2" fill="#E8D27A"/>' for x, y in [(80, gm-3), (120, gm-3), (81, gm+7), (119, gm+7)])
    return (f'<svg viewBox="0 0 200 250" aria-hidden="true" focusable="false">'
            f'<path d="{bone_l}" fill="{BONE}"/><path d="{bone_r}" fill="{BONE}"/>'
            f'<path d="{left}" fill="{gum_c}"/><path d="{right}" fill="{gum_c}"/>'
            f'<rect x="86" y="{imp_top}" width="28" height="120" rx="6" fill="#C9D2D9" stroke="{LINE}" stroke-width="2"/>{threads}'
            f'<rect x="90" y="60" width="20" height="38" fill="#B7C2CB" stroke="{LINE}" stroke-width="2"/>'
            f'<path d="M64,56 Q64,14 100,14 Q136,14 136,56 Z" fill="#fff" stroke="{LINE}" stroke-width="2.5"/>{extra}</svg>')

def implant_triptych(items, caption, label="Schémas autour de l'implant"):
    out = "".join(f'<figure class="tri"><div class="tri-art">{_implant_state(k)}</div><figcaption>{t}</figcaption></figure>' for k, t in items)
    legend = ('<p class="tri-legend"><span class="lg lg-gum"></span>Gencive '
              '<span class="lg lg-bone"></span>Os '
              '<span class="lg lg-plaque"></span>Plaque</p>')
    return figure(f'<div class="tri-grid">{out}</div>{legend}', caption, "fig-tri", label)

def _retention(kind):
    """kind : 'vissee' ou 'scellee'."""
    base = ('<rect x="64" y="150" width="72" height="76" rx="8" fill="#C9D2D9" stroke="#6F8293" stroke-width="2"/>'
            '<rect x="84" y="100" width="32" height="52" fill="#B7C2CB" stroke="#6F8293" stroke-width="2"/>')
    crown = '<path d="M50,100 Q50,24 100,24 Q150,24 150,100 Z" fill="#fff" stroke="#6F8293" stroke-width="2.5"/>'
    if kind == "vissee":
        extra = ('<rect x="94" y="24" width="12" height="96" fill="#F4F7F9" stroke="#6F8293" stroke-width="1.5"/>'
                 '<rect x="96" y="60" width="8" height="70" fill="#3E5568"/>'
                 '<rect x="93" y="54" width="14" height="8" rx="2" fill="#3E5568"/>'
                 '<rect x="92" y="22" width="16" height="8" rx="2" fill="#2C749A"/>')
    else:
        extra = ('<path d="M84,100 L116,100" stroke="#E0B84A" stroke-width="7" stroke-linecap="round"/>'
                 '<circle cx="124" cy="104" r="6" fill="#E0B84A"/>')
    return f'<svg viewBox="0 0 200 250" aria-hidden="true" focusable="false">{base}{crown}{extra}</svg>'

def retention_pair(caption, label="Prothèse vissée et prothèse scellée"):
    out = (f'<figure class="tri"><div class="tri-art">{_retention("scellee")}</div><figcaption><strong>Scellée</strong><br>La couronne est collée sur le pilier avec un ciment (en jaune).</figcaption></figure>'
           f'<figure class="tri"><div class="tri-art">{_retention("vissee")}</div><figcaption><strong>Vissée</strong><br>La couronne est fixée par une vis, accessible par un petit orifice refermé ensuite.</figcaption></figure>')
    return figure(f'<div class="tri-grid tri-two">{out}</div>', caption, "fig-tri", label)
