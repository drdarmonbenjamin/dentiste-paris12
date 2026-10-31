# Site du Dr Benjamin Darmon — dentiste-paris12.com

## Mise en ligne chez OVH

Le site est 100 % statique (HTML/CSS/JS, aucun PHP, aucune base de données), il fonctionne donc sur **n'importe quelle offre d'hébergement mutualisé OVH**, y compris la plus basique.

**Étapes :**

1. **Récupérez vos identifiants FTP** : dans l'espace client OVHcloud → *Hébergements* → votre hébergement → onglet *FTP-SSH*. Vous y trouverez le nom d'hôte (serveur), l'identifiant et pouvez réinitialiser le mot de passe FTP si besoin.

2. **Connectez-vous en (S)FTP.** Deux options :
   - **FileZilla** (recommandé) : renseignez hôte / identifiant / mot de passe / port dans la barre de connexion rapide.
   - **Explorateur FTP intégré** : directement depuis l'espace client OVHcloud (*Hébergements* → votre hébergement → *Gérer mon espace* / *FTP-SSH* → *Explorateur de fichiers*), sans rien installer.

3. **Déposez tout le contenu du zip dans le dossier `www`** à la racine de votre espace d'hébergement (c'est le dossier public d'OVH — tout ce qui est en dehors n'est pas accessible depuis le web). Glissez-déposez l'ensemble des fichiers et dossiers (`index.html`, `css/`, `js/`, `images/`, etc.) directement dedans, pas dans un sous-dossier.

4. **⚠️ Si un site existait déjà dans ce dossier `www`** (par exemple l'ancien WordPress) : videz-le d'abord entièrement, sinon d'anciens fichiers (comme un `index.php`) pourraient entrer en conflit avec le nouveau `index.html` et s'afficher à la place. Sauvegardez l'ancien site avant de le supprimer si vous voulez garder une copie.

5. **Vérifiez le HTTPS** : dans l'espace client OVHcloud → votre hébergement → onglet *SSL/TLS*, le certificat Let's Encrypt gratuit doit être actif (généralement automatique). Si le site s'affiche en `http://` non sécurisé après mise en ligne, c'est le premier endroit à vérifier.

6. **Le nom de domaine** dentiste-paris12.com doit déjà pointer vers cet hébergement s'il y était avant. S'il est ailleurs, il faut le rattacher à votre hébergement OVH (espace client → *Noms de domaine* → *Zone DNS*, ou *Multidomaine* dans l'hébergement si le domaine est aussi chez OVH).

## Après la mise en ligne
- Complétez la ligne « Hébergement » dans `mentions-legales.html` (déjà chez OVH, précisez la raison sociale : OVHcloud, 2 rue Kellermann, 59100 Roubaix).
- Soumettez `sitemap.xml` dans Google Search Console et Bing Webmaster Tools.
- Vérifiez que votre fiche Google Business Profile utilise la même adresse exacte que le site.
- Testez le formulaire de contact une fois en ligne (il envoie vers drdarmonbenjamin@gmail.com via Web3Forms).

## Toujours en attente de votre côté
- Confirmation sur l'image fluor (mention de copyright Adobe Stock trouvée dans ses métadonnées) — le fluor affiche pour l'instant une image libre de droit de remplacement.
- Photo de Nadia Buta.
- Numéro d'inscription à l'Ordre National des Chirurgiens-Dentistes, si vous voulez qu'il soit affiché en plus du RPPS.

## Blog (publication automatique, un article par semaine)

Le site contient un blog de 13 articles sur la parodontologie et l'implantologie, accessible uniquement par le lien « Blog » du pied de page. Les articles sont signés du Dr Benjamin Darmon et citent leurs sources. Ils ne mentionnent aucune validation par un tiers.

**Planification.** Il suffit de déposer le site une seule fois. Chaque article porte une date de publication (un lundi par semaine, du 9 novembre 2026 au 1er février 2027) :

- avant sa date, l'article renvoie une erreur 404 (règle écrite dans `.htaccess`, entre les lignes `BLOG-PLANNING-DEBUT` et `BLOG-PLANNING-FIN`, selon l'heure du serveur) ;
- la page Blog et les liens « À lire également » masquent les articles à venir (petit script dans la page) ;
- le plan du site pour les moteurs de recherche, `sitemap-blog.php` (déclaré dans `robots.txt`), ne liste que les articles déjà publiés.

Après la mise en ligne, tester une fois : ouvrir l'adresse d'un article futur (par exemple `/blog/parodontite-comprendre-la-maladie-des-gencives`) doit afficher une erreur 404 tant que sa date de publication (23 novembre 2026 pour cet exemple) n'est pas atteinte. Si la page s'affiche, la règle `RewriteCond %{TIME}` n'est pas appliquée par l'hébergement : le dire à Claude.

**Limite à connaître.** Le contenu est figé au moment du dépôt. La mise à jour de l'actualité (recommandations HAS, remboursement, etc.) n'est pas automatique : les sources ont été vérifiées le 31 octobre 2026 (`VERIF_DATE`). Avant d'élargir la publication, faire revérifier les articles sensibles au temps, surtout l'article 9 (remboursement des implants) et l'article 1 (antibiotiques).

**Photos des articles.** Chaque article a une photo de couverture, reprise en vignette cliquable dans l'index du blog dès que l'article est publié. Les fichiers sont dans `blog/img/` (`<nom-de-l-article>-1200.jpg` pour l'article et le partage, `-640.jpg` pour la vignette). Ce sont des photos libres de droits (licence Pexels : usage commercial autorisé, mention non obligatoire, mais le crédit figure sous chaque photo et dans le dossier de relecture). Ce sont des objets, maquettes et instruments, jamais des patients : elles illustrent le sujet sans montrer un cas réel. Pour changer une photo : déposer les deux JPEG (1200 x 630 et 640 x 336) dans `blog/img/` sous le même nom, puis corriger son crédit dans `blog-interne/_outils/photos_blog.py` et relancer le script. Les photos sont des fichiers fixes : le script ne les recalcule pas.

**Dossier interne** `blog-interne/` : accès refusé aux visiteurs par son propre `.htaccess`. Il contient le générateur (`_outils/generer_blog.py`), les articles sources (`articles_blog_1.py`, `articles_blog_2.py`), leurs enrichissements (`enrichissements_blog_1.py`, `enrichissements_blog_2.py` : figures, sections complémentaires, glossaire, questions à poser, questions fréquentes, titre et description pour les moteurs de recherche), les composants visuels (`visuels_blog.py`), la bibliographie (`refs_blog.py`) et `dossier-relecture.html` (chaque affirmation reliée à sa source, bibliographie avec son état de vérification, synthèse des revues critiques). Pour le lire, ouvrir le fichier depuis le dossier décompressé du site.

**Modifier un article ou une date.** Corriger le texte dans `articles_blog_1.py` ou `articles_blog_2.py` (ou dans les fichiers d'enrichissements pour les figures, le glossaire et la FAQ ; ou la date `date="AAAA-MM-JJ"`), puis lancer `python3 blog-interne/_outils/generer_blog.py` (ou le demander à Claude). Le script régénère les pages du blog, la règle `.htaccess`, `sitemap-blog.php` et le dossier de relecture. Mettre à jour `VERIF_DATE` dans le script après une nouvelle vérification des sources.
