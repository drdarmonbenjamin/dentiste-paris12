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
