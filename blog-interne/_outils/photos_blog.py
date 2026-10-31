# -*- coding: utf-8 -*-
"""Illustrations des articles du blog : fichiers, textes alternatifs et origine.

Les images ont été générées par intelligence artificielle (ChatGPT) à partir de prompts rédigés pour la charte
graphique du site, puis recadrées (1200 x 630 pour l'article et le partage, 640 x 336 pour la vignette de l'index).
Elles sont dans blog/img/. Choix déontologique : aucun patient identifiable, aucun avant/après, aucune marque ni texte.
Rappel : une illustration générée peut comporter des inexactitudes anatomiques. Le Dr Darmon les valide avant publication.
"""
ORIGINE = "Illustration générée par intelligence artificielle"

def _p(alt, note=""):
    return dict(alt=alt, origine=ORIGINE, note=note)

PHOTOS = {
"antibiotiques-chez-le-dentiste-ce-que-recommande-la-has": _p(
    "Illustration : flacon et plaquette de gélules bleues et blanches, une dent sur sa gencive et des instruments de soins dentaires"),
"gencives-qui-saignent-la-gingivite": _p(
    "Illustration : trois dents avec de la plaque jaunâtre au collet et une gencive rouge et gonflée"),
"parodontite-comprendre-la-maladie-des-gencives": _p(
    "Illustration en coupe : trois dents avec de la plaque, une gencive rouge et un os qui a reculé entre les racines"),
"traiter-une-parodontite-les-quatre-etapes": _p(
    "Image : brosse à dents à poils bleus posée devant un modèle d'arcade dentaire à la gencive rose",
    "Image provisoire : elle illustre la première étape (contrôle de la plaque) ; une illustration des quatre étapes pourra la remplacer."),
"le-surfacage-radiculaire-recommandations-europeennes": _p(
    "Illustration en quatre vignettes : une dent entartrée, le passage d'une curette sous la gencive, puis la racine propre et la gencive qui retrouve sa forme"),
"parodontite-et-diabete-un-lien-dans-les-deux-sens": _p(
    "Illustration : une dent dont la gencive a reculé, une goutte et un lecteur de glycémie, reliés par un trait"),
"parodontite-et-sante-du-coeur-consensus-europeen": _p(
    "Illustration : une dent dont la gencive a reculé et un cœur avec le détail d'une artère, reliés par une traînée de particules"),
"apres-le-traitement-parodontal-la-maintenance": _p(
    "Illustration : main gantée passant une brossette interdentaire entre deux dents d'un modèle, avec un miroir dentaire et un calendrier"),
"implant-dentaire-le-parcours-evalue-par-la-has": _p(
    "Illustration en quatre vignettes : l'espace laissé par une dent absente, la pose de l'implant, le pilier, puis la couronne"),
"implants-dentaires-survie-a-dix-ans-que-disent-les-etudes": _p(
    "Illustration en coupe : un implant en titane surmonté d'une couronne, entre deux dents naturelles, dans l'os et la gencive"),
"peut-on-poser-un-implant-apres-une-parodontite": _p(
    "Illustration en quatre vignettes : une dent atteinte par la parodontite, la gencive et l'os cicatrisés, la pose de l'implant, puis la couronne"),
"peri-implantite-reconnaitre-prevenir-traiter": _p(
    "Illustration : un implant dont la gencive est enflammée et l'os a reculé, avec un agrandissement, puis trois vignettes de traitement jusqu'à une gencive saine"),
"prothese-sur-implant-vissee-ou-scellee": _p(
    "Illustration en coupe : à gauche une couronne fixée par une vis sur un implant, à droite une couronne scellée avec du ciment"),
}
