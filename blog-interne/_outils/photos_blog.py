# -*- coding: utf-8 -*-
"""Photos des articles du blog : fichiers, textes alternatifs, sources et licences.

Les fichiers recadrés (1200 x 630 et 640 x 336) sont dans blog/img/. Les originaux restent chez leur source.
Choix déontologique : objets, maquettes et instruments uniquement, aucune photo de patient identifiable,
aucun avant/après, aucun produit de marque lisible.
Licence Pexels : usage libre, y compris commercial, sans obligation de mention (https://www.pexels.com/license/).
"""
PEXELS = "Pexels (licence libre)"
LICENCE_URL = "https://www.pexels.com/license/"

def _p(pid, slugpage, auteur, alt):
    return dict(page=f"https://www.pexels.com/photo/{slugpage}-{pid}/", auteur=auteur, alt=alt, licence=PEXELS, licence_url=LICENCE_URL)

PHOTOS = {
"antibiotiques-chez-le-dentiste-ce-que-recommande-la-has": _p("30336386", "close-up-of-blister-pack-with-pills-on-wooden-surface", "Christina & Peter",
    "Plaquette de gélules transparentes posée sur une surface en bois sombre"),
"gencives-qui-saignent-la-gingivite": _p("13579612", "toothbrush-on-white-surface", "Andrew Patrick Photo",
    "Brosse à dents à poils bleus et blancs posée sur une surface blanche"),
"parodontite-comprendre-la-maladie-des-gencives": _p("7422519", "teeth-and-dental-cast-models", "Emeric Kalil",
    "Modèles pédagogiques de dents et de gencives sur une étagère"),
"traiter-une-parodontite-les-quatre-etapes": _p("6627668", "a-close-up-shot-of-dental-equipment", "Kaboompics",
    "Instruments d'une unité de soins dentaires et plateau métallique"),
"le-surfacage-radiculaire-recommandations-europeennes": _p("12374355", "dental-scaler-on-turquoise-background", "Anna Astakhova",
    "Instrument dentaire manuel à pointe courbe sur fond turquoise"),
"parodontite-et-diabete-un-lien-dans-les-deux-sens": _p("17071587", "a-blood-glucose-meter-a-pill-and-a-bottle-of-water", "i-SENS, USA",
    "Lecteur de glycémie, stylo autopiqueur et bandelettes posés sur une table en bois"),
"parodontite-et-sante-du-coeur-consensus-europeen": _p("5207102", "part-of-a-person-with-a-stethoscope", "Kaboompics",
    "Blouse de soignant vert d'eau avec un stéthoscope et un cœur en papier dans la poche"),
"apres-le-traitement-parodontal-la-maintenance": _p("6502308", "close-up-shot-of-dentures", "cottonbro studio",
    "Modèle de mâchoire en résine avec un fil dentaire passé entre les dents"),
"implant-dentaire-le-parcours-evalue-par-la-has": _p("39377366", "dental-implant-prosthetics-on-blue-background", "Zeynep Kahraman",
    "Prothèse dentaire sur implants avec ses piliers métalliques, sur fond bleu"),
"implants-dentaires-survie-a-dix-ans-que-disent-les-etudes": _p("6502305", "close-up-shot-of-dental-implant-model", "cottonbro studio",
    "Maquette pédagogique montrant un implant dans l'os et la gencive"),
"peut-on-poser-un-implant-apres-une-parodontite": _p("4270367", "an-ipad-showing-the-x-ray-of-teeth", "Cedric Fauntleroy",
    "Mains gantées tenant une tablette qui affiche une radiographie panoramique des dents"),
"peri-implantite-reconnaitre-prevenir-traiter": _p("4687905", "dental-implants-with-screw-on-table-in-clinic", "Jonathan Borba",
    "Maquette en coupe de dents et d'un implant dans l'os et la gencive"),
"prothese-sur-implant-vissee-ou-scellee": _p("6502343", "close-up-shot-of-dental-implant-model", "cottonbro studio",
    "Maquette d'implant avec la couronne posée à côté du pilier"),
}
