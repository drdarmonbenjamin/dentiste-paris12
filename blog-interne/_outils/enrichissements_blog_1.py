# -*- coding: utf-8 -*-
"""Enrichissements des articles 1 à 7 : visuels, sections complémentaires, glossaire, questions fréquentes.

Chaque affirmation nouvelle reprend une source déjà citée dans l'article (voir claims_more).
"""
from visuels_blog import *

ENRICH_1 = {}

# ------------------------------------------------------------------ 1
ENRICH_1["antibiotiques-chez-le-dentiste-ce-que-recommande-la-has"] = dict(
seo_title="Antibiotiques dentaires : la HAS en 2026",
meta="Gencives, parodontite, implants : ce que la HAS recommande en 2026 sur les antibiotiques en soins dentaires, expliqué simplement pour les patients.",
figs={
"principes": flow([
 ("Le praticien cherche la cause", "Une douleur dentaire est le plus souvent d'origine inflammatoire : l'examen sert à trouver l'origine du problème."),
 ("Un geste local d'abord", "Traiter la cause (par exemple drainer une infection) est la base de la prise en charge, avec un antalgique adapté."),
 ("Un antibiotique si la situation le justifie", "Dans des cas précis seulement, et toujours en complément du geste local."),
 ("Un point à 2 ou 3 jours", "Le traitement est réévalué. Un traitement court peut donner des résultats comparables à un traitement plus long."),
], "Le raisonnement général décrit par la HAS : l'antibiotique accompagne le geste local, il ne le remplace pas."),
"gencives": verdict_table([
 ("Détartrage et surfaçage radiculaire (population générale)", "non", "Peut être recommandé au cas par cas chez les patients à risque infectieux augmenté."),
 ("Gingivite", "non", ""),
 ("Parodontite, hors cas particuliers", "non", ""),
 ("Parodontite de stade III ou IV avec destruction plus importante que la plaque ne le laisse prévoir", "oui", "Après la dernière séance de surfaçage (accord d'experts)."),
 ("Poches résiduelles", "non", ""),
 ("Abcès parodontal", "cas", "En général non, sauf patients à risque, signes d'extension de l'infection ou geste local impossible."),
 ("Antibiotique appliqué localement", "non", "Quels que soient le traitement ou la pathologie."),
], "Les gencives : ce que la HAS recommande pour l'antibiotique (tableaux de la recommandation de 2026).", head=("Situation", "Position de la HAS")),
"implants": verdict_table([
 ("Pose d'implants (population générale)", "cas", "Pas d'antibioprophylaxie systématique : elle dépend du profil du patient et de la complexité de l'intervention."),
 ("Greffe osseuse avant ou pendant la pose, élévation du sinus", "oui", "Antibioprophylaxie recommandée dans la population générale."),
 ("Mucosite péri-implantaire", "non", ""),
 ("Péri-implantite", "cas", "Non recommandé, sauf cas particuliers."),
], "Les implants : ce que la HAS recommande pour l'antibiotique.", head=("Situation", "Position de la HAS")),
},
more=[
("pratique", "Que faire en pratique ?",
 """<p>Cette recommandation s'adresse aux professionnels, mais elle a des conséquences concrètes pour vous :</p>
<ul class="check-list">
<li><strong>Signalez vos traitements et vos maladies.</strong> Un diabète mal contrôlé, des défenses immunitaires affaiblies, une radiothérapie de la tête et du cou ou certains médicaments contre le cancer ou l'ostéoporose peuvent changer la décision.</li>
<li><strong>Ne prenez pas d'antibiotique de votre initiative</strong>, même s'il vous en reste d'un traitement précédent, et ne l'arrêtez pas sans l'avis d'un professionnel de santé.</li>
<li><strong>Attendez-vous à un geste local.</strong> Lorsqu'il y a une infection, la HAS place le geste qui traite la cause avant l'antibiotique.</li>
<li><strong>Reprenez contact si les symptômes persistent ou s'aggravent.</strong> La recommandation prévoit un point 2 à 3 jours après le début d'un traitement.</li>
</ul>"""),
("difference", "Antibiotique pour soigner, antibiotique pour prévenir : quelle différence ?",
 """<p>Deux usages sont à distinguer. L'antibiotique <strong>curatif</strong> traite une infection déjà présente. L'<strong>antibioprophylaxie</strong> est un antibiotique pris <em>avant</em> un acte, pour prévenir une infection. C'est cette seconde forme qui fait l'objet des tableaux de la HAS pour le détartrage, le surfaçage et la pose d'implants : elle ne doit pas être systématique et n'est indiquée que dans des situations précises, selon l'acte et le profil du patient.</p>"""),
],
gloss=[
 ("Antibioprophylaxie", "Antibiotique pris avant un acte pour prévenir une infection."),
 ("Antibiorésistance", "Perte d'efficacité des antibiotiques, favorisée par un usage excessif ou inapproprié."),
 ("Antibiothérapie locale", "Antibiotique appliqué directement à l'endroit à traiter. La HAS recommande de ne pas l'utiliser en pratique bucco-dentaire."),
 ("Ostéonécrose des mâchoires", "Atteinte de l'os de la mâchoire. Le risque est augmenté par certains traitements, comme une radiothérapie de la tête et du cou ou certains médicaments contre le cancer ou l'ostéoporose. Les patients concernés font l'objet de règles particulières dans la recommandation."),
 ("Mucosite péri-implantaire", "Inflammation de la gencive autour d'un implant, sans perte osseuse au-delà du remodelage initial."),
],
ask=[
 "Un antibiotique est-il nécessaire dans ma situation, et pourquoi ?",
 "Quel geste local allez-vous réaliser pour traiter la cause ?",
 "Ai-je une maladie ou un traitement à vous signaler avant ce soin ?",
 "Quand dois-je vous recontacter si les symptômes persistent ?",
],
faq=[
 ("Le dentiste doit-il toujours prescrire un antibiotique en cas de douleur dentaire ?",
  "Non. Selon la HAS, une douleur dentaire est le plus souvent d'origine inflammatoire et ne justifie pas, à elle seule, un antibiotique. La prise en charge repose d'abord sur un geste local qui traite la cause, avec un antalgique adapté."),
 ("Faut-il un antibiotique pour une gingivite ou une parodontite ?",
  "La HAS ne le recommande ni pour la gingivite ni pour la parodontite hors cas particuliers. Une exception existe pour certaines parodontites de stade III ou IV, lorsque la destruction est plus importante que la quantité de plaque ne le laisse prévoir. La décision revient au praticien qui vous examine."),
 ("Faut-il un antibiotique avant la pose d'un implant ?",
  "Pas de façon systématique dans la population générale, selon la HAS : cela dépend du profil du patient et de la complexité de l'intervention. Pour une greffe osseuse ou une élévation du sinus, une antibioprophylaxie est recommandée. Une revue Cochrane de septembre 2026 suggère un bénéfice d'une prise avant la pose : votre chirurgien-dentiste décide selon votre situation."),
 ("Puis-je prendre un antibiotique sans ordonnance ou arrêter plus tôt ?",
  "Non. Ne prenez pas et n'arrêtez pas un antibiotique sans l'avis d'un professionnel de santé. Les molécules, les doses et les durées relèvent de la prescription du praticien, qui adapte la recommandation à chaque patient."),
 ("Pourquoi limiter les antibiotiques en soins dentaires ?",
  "Un usage excessif ou inapproprié des antibiotiques favorise l'antibiorésistance, c'est-à-dire la perte d'efficacité de ces médicaments. La HAS a donc voulu harmoniser les pratiques chez l'adulte comme chez l'enfant."),
 ("Que dois-je dire à mon dentiste avant un soin ?",
  "Signalez vos maladies, vos traitements en cours, vos allergies et tout traitement reçu au niveau de la tête et du cou. La décision d'utiliser ou non un antibiotique en dépend."),
],
claims_more=[
 ("Schéma du raisonnement (cause, geste local, antibiotique si justifié, point à 2-3 jours) : reprend les principes généraux déjà sourcés dans le corps de l'article.","HAS_ATB_COMM","Communiqué, messages principaux ; HAS_ATB_2026 p. 23, 30-32"),
 ("Définitions du glossaire (antibioprophylaxie, antibiorésistance, antibiothérapie locale, ostéonécrose) : reprennent les formulations du corps de l'article.","HAS_ATB_2026","PDF, p. 9 et section 6"),
 ("Mucosite péri-implantaire : inflammation sans perte osseuse au-delà du remodelage initial.","BERG_2018","Définitions"),
],
)

# ------------------------------------------------------------------ 2
ENRICH_1["gencives-qui-saignent-la-gingivite"] = dict(
seo_title="Gencives qui saignent : la gingivite",
meta="Gencives rouges ou qui saignent au brossage ? Ce qu'est la gingivite, comment on la repère, ce qu'on peut faire et pourquoi elle est réversible.",
figs={
"definition": tooth_triptych([
 ("sain", "<strong>Gencive saine</strong><br>Ni rougeur, ni gonflement, ni saignement au sondage doux."),
 ("gingivite", "<strong>Gingivite</strong><br>Gencive rouge, gonflée, qui saigne. Elle reste limitée à la gencive."),
 ("parodontite", "<strong>Parodontite</strong><br>Les tissus de soutien sont atteints : perte d'attache et d'os."),
], "Schémas simplifiés d'une dent dans sa gencive. Seule la gingivite est réversible par la maîtrise de la plaque.", label="Gencive saine, gingivite et parodontite"),
"diagnostic": scale([
 ("moins de 10 %", "des sites saignent : en dessous du seuil de référence", 0),
 ("10 à 30 %", "des sites saignent : gingivite localisée", 2),
 ("plus de 30 %", "des sites saignent : gingivite généralisée", 3),
], "Les seuils de référence utilisés par les professionnels (pourcentage de sites qui saignent au sondage doux).", label="Seuils de saignement"),
},
more=[
("difference", "Gingivite ou parodontite : quelle différence ?",
 cards([
  ("Gingivite", "Inflammation limitée à la gencive, sans perte d'attache ni d'os. Réversible lorsque la plaque est réduite."),
  ("Parodontite", "Inflammation qui détruit les tissus de soutien de la dent. Elle demande un traitement par étapes."),
 ], "La différence tient à l'atteinte (ou non) des tissus de soutien.", label="Gingivite et parodontite") +
 """<p>Seul un examen permet de faire la différence : le chirurgien-dentiste sonde doucement autour des dents. Les radiographies ne permettent pas de diagnostiquer une gingivite. Pour la suite, voir l'article « La parodontite : comprendre la maladie des gencives et de l'os ».</p>"""),
("quand", "Quand consulter ?",
 """<ul class="check-list">
<li>dès l'apparition de signes : gencives rouges ou gonflées, saignements ;</li>
<li>si les saignements persistent malgré un brossage régulier ou s'accompagnent d'autres signes ;</li>
<li>si vous avez déjà été traité pour une parodontite : une inflammation de la gencive signale alors un risque de récidive ;</li>
<li>même sans symptôme, pour un contrôle au moins une fois par an.</li>
</ul>"""),
],
gloss=[
 ("Plaque dentaire (biofilm)", "Dépôt de bactéries organisées qui se forme sur les dents et à la limite de la gencive."),
 ("Sondage parodontal", "Examen où le praticien glisse doucement une sonde graduée entre la dent et la gencive pour repérer saignement et profondeur."),
 ("Gingivite", "Inflammation de la gencive provoquée par la plaque, réversible, sans perte d'attache."),
 ("Parodonte", "Ensemble des tissus qui soutiennent la dent : gencive, os, ligament et cément."),
 ("Parodonte réduit", "Situation d'une personne déjà traitée pour une parodontite, dont les tissus de soutien ont diminué."),
],
ask=[
 "Mes gencives saignent : s'agit-il d'une gingivite ou d'autre chose ?",
 "Mon brossage est-il efficace ? Pouvez-vous me montrer la méthode adaptée à ma bouche ?",
 "Quelle brossette ou quel autre dispositif interdentaire convient à mes espaces ?",
 "À quelle fréquence dois-je faire contrôler mes gencives ?",
],
faq=[
 ("Pourquoi mes gencives saignent-elles quand je me brosse les dents ?",
  "Le plus souvent, parce que la plaque dentaire a provoqué une inflammation de la gencive : c'est la gingivite. Toutes les gencives qui saignent ne sont toutefois pas dues à la plaque : si le saignement persiste malgré un brossage régulier, consultez."),
 ("Une gingivite est-elle réversible ?",
  "Oui. Selon le consensus de 2017, la gingivite reste limitée à la gencive et elle régresse lorsqu'on réduit la plaque au niveau de la gencive et en dessous."),
 ("Faut-il arrêter de se brosser les dents quand la gencive saigne ?",
  "Non. Ne cessez pas de vous brosser les dents : le saignement régresse en général quand la plaque est mieux maîtrisée."),
 ("La gingivite se soigne-t-elle avec un antibiotique ?",
  "Non. La HAS ne recommande pas d'antibiotique pour traiter une gingivite (recommandation de septembre 2026). La décision appartient toujours au praticien qui vous examine."),
 ("À quelle fréquence faire contrôler ses gencives ?",
  "Les consensus d'experts conseillent un contrôle au moins une fois par an, même sans symptôme. Votre praticien adapte ce rythme à votre situation."),
 ("Une gingivite peut-elle revenir après un traitement de parodontite ?",
  "Oui, et il faut la prendre au sérieux : chez une personne traitée pour une parodontite, une inflammation de la gencive ne doit pas être considérée comme une simple gingivite, car elle signale un risque de récidive."),
],
claims_more=[
 ("Gingivite : pas de perte d'attache ni d'os ; diagnostic non radiographique ; seuils 10 % / 30 %.","CHAPPLE_2018","Section gingivite"),
],
)

# ------------------------------------------------------------------ 3
ENRICH_1["parodontite-comprendre-la-maladie-des-gencives"] = dict(
seo_title="Parodontite : la maladie des gencives",
meta="Stades, grades, signes d'alerte : ce qu'est la parodontite, comment elle est classée et repérée, et pourquoi un contrôle annuel est conseillé.",
figs={
"classification": cards([
 ("Le stade (I à IV)", "Gravité de la maladie au moment du diagnostic et complexité de sa prise en charge."),
 ("Le grade (A à C)", "Vitesse de progression, risque d'évolution, risque d'échec du traitement et effet possible sur la santé générale."),
], "Chaque cas de parodontite reçoit un stade et un grade, selon la classification de 2017.", label="Stade et grade"),
"signes": tooth_triptych([
 ("sain", "<strong>Dent saine</strong><br>Gencive adhérente et os de soutien intact."),
 ("parodontite", "<strong>Parodontite</strong><br>Poche entre la dent et la gencive, perte osseuse, tartre sous la gencive."),
], "Schémas simplifiés : dans la parodontite, la destruction de l'os de soutien peut avancer sans douleur.", label="Dent saine et parodontite"),
},
more=[
("silence", "Pourquoi consulter même sans douleur ?",
 """<p>La maladie peut progresser silencieusement : l'absence de douleur ne signifie pas l'absence de maladie. C'est la raison pour laquelle les consensus d'experts conseillent un contrôle annuel, même sans symptôme. Seul un examen permet de poser un diagnostic et de déterminer le stade et le grade.</p>"""),
("prevention", "Ce que vous pouvez faire dès maintenant",
 """<ul class="check-list">
<li>Faire contrôler vos gencives au moins une fois par an, même sans symptôme.</li>
<li>Consulter dès l'apparition de gencives rouges ou gonflées, de saignements, d'une dent qui bouge ou d'espaces qui augmentent entre les dents.</li>
<li>Demander de l'aide pour arrêter de fumer : l'aide à l'arrêt du tabac fait partie des mesures recommandées.</li>
<li>Si vous êtes diabétique, en parler à votre dentiste et à votre médecin : la prise en charge du diabète fait aussi partie des mesures recommandées.</li>
</ul>"""),
],
gloss=[
 ("Parodontite", "Maladie inflammatoire qui détruit peu à peu les tissus de soutien de la dent (gencive, os, ligament)."),
 ("Stade", "Niveau de gravité de la parodontite au moment du diagnostic (de I à IV)."),
 ("Grade", "Information sur la vitesse de progression et les risques associés (de A à C)."),
 ("Abcès parodontal", "Accumulation localisée de pus dans la paroi de la gencive, avec destruction rapide des tissus. Il doit être examiné rapidement."),
 ("Lésion endo-parodontale", "Communication anormale entre les tissus de la pulpe (l'intérieur de la dent) et ceux du parodonte."),
],
ask=[
 "Quels sont mon stade et mon grade, et que signifient-ils pour mon traitement ?",
 "Comment ma maladie sera-t-elle suivie dans le temps ?",
 "Mon tabac ou mon diabète jouent-ils un rôle, et comment être aidé ?",
 "Quels signes doivent me faire reprendre rendez-vous sans attendre ?",
],
faq=[
 ("Qu'est-ce que la parodontite ?",
  "C'est une maladie inflammatoire qui détruit peu à peu les tissus de soutien de la dent. Depuis la classification de 2018, les anciennes formes « chronique » et « agressive » sont regroupées sous ce seul terme, décrit par un stade et un grade."),
 ("Quels sont les signes d'une parodontite ?",
  "Gencives rouges ou gonflées, saignements, dents qui se déchaussent ou qui bougent, espaces qui augmentent entre les dents, mauvaise haleine ou goût désagréable, tartre. Ces signes ne suffisent pas à poser un diagnostic : seul un examen le permet."),
 ("La parodontite fait-elle mal ?",
  "Pas forcément. La maladie peut progresser sans symptôme, ce qui explique qu'un contrôle annuel soit conseillé même en l'absence de gêne."),
 ("Quelle différence entre gingivite et parodontite ?",
  "La gingivite reste limitée à la gencive, sans perte d'attache ni d'os, et elle est réversible. Dans la parodontite, les tissus de soutien de la dent sont atteints."),
 ("Le tabac et le diabète jouent-ils un rôle ?",
  "Les recommandations européennes de 2020 incluent, dès la première étape du traitement, l'aide à l'arrêt du tabac et la prise en charge du diabète."),
 ("Comment pose-t-on le diagnostic ?",
  "Seul un examen le permet. Le stade et le grade sont ensuite précisés pour chaque patient par le praticien."),
],
claims_more=[
  ("Stades I à IV, grades A à C.","PAPA_2018","Résumé du consensus"),
],
)

# ------------------------------------------------------------------ 4
ENRICH_1["traiter-une-parodontite-les-quatre-etapes"] = dict(
seo_title="Traiter une parodontite en 4 étapes",
meta="Contrôle de la plaque, surfaçage, traitement des sites résistants, soins de soutien : les quatre étapes recommandées par l'EFP pour traiter la parodontite.",
figs={
"etape3": verdict_table([
 ("Répéter l'instrumentation des sites qui n'ont pas répondu", "cas", "Une des options possibles."),
 ("Chirurgie d'accès ou résective, pour les poches de 6 mm ou plus", "sug", ""),
 ("Chirurgie régénérative, pour une poche profonde en regard d'un défaut osseux de 3 mm ou plus", "oui", ""),
 ("Chirurgie lorsque l'hygiène bucco-dentaire du patient est insuffisante", "non", ""),
 ("Extraction décidée sur la seule atteinte de la furcation", "non", "Elle n'est pas, à elle seule, une indication d'extraction."),
], "Étape 3 : ce que précisent les recommandations pour les sites qui n'ont pas répondu au traitement.", head=("Pratique", "Position"), label="Étape 3 : les options"),
"methode": flow([
 ("Maîtriser la plaque et les facteurs de risque", "Pour tous les patients : hygiène efficace, retrait professionnel de la plaque et du tartre au-dessus de la gencive, aide à l'arrêt du tabac, contrôle du diabète."),
 ("Traiter sous la gencive", "Surfaçage : retrait de la plaque et du tartre situés sous la gencive. Réévaluation à la fin de l'étape."),
 ("Traiter les sites qui n'ont pas répondu", "Nouvelle instrumentation ou chirurgie, selon la situation de chaque site."),
 ("Soins de soutien", "Visites régulières, espacées de 3 à 12 mois selon le profil de risque, pour éviter la récidive."),
], "Les quatre étapes de la recommandation européenne de 2020 pour les parodontites de stades I à III.", label="Les quatre étapes du traitement"),
},
more=[
("patient", "Votre rôle à chaque étape",
 """<p>Les recommandations européennes insistent sur l'engagement du patient : les mêmes conseils d'hygiène sont donnés à toutes les étapes, et l'adhésion au programme de soins est recommandée. La chirurgie est déconseillée lorsque l'hygiène bucco-dentaire est insuffisante : le traitement ne repose donc pas que sur le cabinet.</p>
<p>Concrètement, la recommandation fixe des objectifs mesurables à la réévaluation : aucune poche de 5 mm ou plus avec saignement, et aucune poche de 6 mm ou plus. Si ces critères sont atteints, le patient passe aux soins de soutien. Sinon, on passe à l'étape 3.</p>"""),
],
gloss=[
 ("Recommandation de niveau S3", "Recommandation élaborée à partir de revues systématiques de la littérature et d'un consensus formalisé d'experts, selon la méthode GRADE."),
 ("Poche parodontale", "Espace qui se creuse entre la dent et la gencive quand les tissus de soutien sont atteints."),
 ("Instrumentation sous-gingivale (surfaçage)", "Retrait de la plaque et du tartre situés sous la gencive, avec éventuellement une partie du cément de la racine."),
 ("Furcation", "Zone située entre les racines d'une molaire. Son atteinte n'est pas, à elle seule, une indication d'extraction."),
 ("Chirurgie régénérative", "Chirurgie qui vise à reconstituer une partie des tissus de soutien perdus."),
],
ask=[
 "À quelle étape en suis-je, et quels objectifs doit-on atteindre à la réévaluation ?",
 "Que dois-je faire à la maison à cette étape ?",
 "Si une poche persiste, quelles options existent pour ce site ?",
 "Quel rythme de visites de soutien me conseillez-vous après le traitement ?",
],
faq=[
 ("Combien d'étapes comprend le traitement d'une parodontite ?",
  "Quatre, selon la recommandation européenne de 2020 pour les stades I à III : maîtrise de la plaque et des facteurs de risque, surfaçage sous la gencive, traitement des sites qui n'ont pas répondu, puis soins de soutien."),
 ("La chirurgie est-elle toujours nécessaire ?",
  "Non. Elle n'intervient qu'à l'étape 3, pour les sites qui n'ont pas répondu au traitement non chirurgical. Elle est déconseillée lorsque l'hygiène du patient est insuffisante."),
 ("Pourquoi faut-il revenir régulièrement après le traitement ?",
  "Parce que les soins de soutien font partie des mesures recommandées pour limiter le risque de récidive et de progression de la maladie. Les visites sont espacées de 3 à 12 mois selon le profil de risque."),
 ("Qu'est-ce qu'une poche qui persiste ?",
  "C'est un site qui n'a pas atteint les objectifs de la réévaluation, par exemple une poche de plus de 4 mm avec saignement ou une poche de 6 mm ou plus. Plusieurs options existent alors : répéter l'instrumentation ou recourir à une chirurgie."),
 ("Et pour les parodontites de stade IV ?",
  "Le stade IV, plus avancé, fait l'objet d'une recommandation distincte de la même fédération, publiée en 2022."),
 ("Une dent dont la furcation est atteinte doit-elle être arrachée ?",
  "Pas automatiquement. Selon les recommandations, l'atteinte de la furcation n'est pas, à elle seule, une indication d'extraction."),
],
claims_more=[
 ("Rôle du patient : mêmes conseils à toutes les étapes, adhésion au programme.","S3_2020","R1.1, R1.2, R4.1"),
 ("Objectifs de réévaluation de l'étape 2 et conséquence (étape 4 ou étape 3).","S3_2020_FIG","Étape 2"),
],
)

# ------------------------------------------------------------------ 5
ENRICH_1["le-surfacage-radiculaire-recommandations-europeennes"] = dict(
seo_title="Surfaçage radiculaire : recommandations",
meta="Surfaçage radiculaire : en quoi consiste-t-il, quels compléments sont recommandés ou non (lasers, antibiotiques, probiotiques) selon l'EFP et la HAS.",
figs={
"recommande": flow([
 ("Le geste", "Retrait de la plaque et du tartre sous la gencive, à la main, aux ultrasons ou en combinant les deux."),
 ("Le rythme", "Par quadrant ou toute la bouche en 24 heures : les deux approches sont possibles."),
 ("L'hygiène à chaque étape", "Mêmes conseils à toutes les étapes, avec un engagement du patient."),
 ("La réévaluation", "À la fin de l'étape, on vérifie si les objectifs sont atteints."),
], "Le surfaçage dans la recommandation européenne de 2020.", label="Le surfaçage en quatre points"),
"complements": verdict_table([
 ("Instrumentation sous-gingivale (surfaçage)", "oui", "Recommandation forte, pour réduire les poches, l'inflammation et le nombre de sites atteints."),
 ("Instruments manuels, soniques, ultrasoniques ou combinaison", "oui", ""),
 ("Traitement par quadrant ou bouche entière en 24 heures", "sug", "Les deux approches sont possibles."),
 ("Lasers et thérapie photodynamique en complément", "nsug", ""),
 ("Antibiotiques par voie générale en routine", "non", "Sauf situations bien définies de parodontite sévère."),
 ("Antibiotiques appliqués localement", "non", "EFP 2020 : laissés au praticien. HAS 2026 : déconseillés en pratique bucco-dentaire."),
 ("Probiotiques", "nsug", ""),
 ("Gels de statines ou de metformine ; bisphosphonates, anti-inflammatoires ou oméga-3 utilisés pour traiter la parodontite", "non", ""),
 ("Chlorhexidine en bain de bouche, pour une durée limitée", "ouv", ""),
], "Surfaçage et compléments : synthèse des recommandations européennes de 2020, complétées par la HAS de 2026.", head=("Pratique", "Position"), label="Surfaçage et compléments"),
},
more=[
("antibiotique", "Faut-il un antibiotique pour un surfaçage ?",
 """<p>Selon la HAS (2026), l'antibioprophylaxie, c'est-à-dire l'antibiotique pris avant le geste, n'est pas recommandée pour le détartrage et le surfaçage dans la population générale. Elle peut être recommandée, au cas par cas, chez les patients à risque infectieux augmenté. Cette décision revient au praticien. Pour le détail, voir l'article « Antibiotiques chez le dentiste : ce que recommande la HAS en 2026 ».</p>"""),
],
gloss=[
 ("Détartrage", "Retrait professionnel de la plaque et du tartre au-dessus de la gencive (première étape du traitement)."),
 ("Surfaçage radiculaire", "Instrumentation sous la gencive qui retire plaque et tartre sur la racine, avec éventuellement une partie du cément."),
 ("Cément", "Fine couche qui recouvre la racine de la dent."),
 ("Thérapie photodynamique", "Technique associant une substance sensibilisante et une lumière, proposée en complément. Elle n'est pas suggérée par les recommandations de 2020."),
 ("Recommandation forte, suggérée, non suggérée", "Niveaux utilisés par les recommandations : forte (à faire), suggérée (peut être proposée), non suggérée (les preuves disponibles ne montrent pas de bénéfice suffisant ; cela ne veut pas dire que c'est dangereux)."),
],
ask=[
 "Le surfaçage sera-t-il fait par quadrant ou sur toute la bouche, et pourquoi ?",
 "Quels compléments éventuels me proposez-vous, et sur quelles preuves ?",
 "À quel moment ferons-nous la réévaluation ?",
 "Que dois-je faire à la maison après chaque séance ?",
],
faq=[
 ("En quoi consiste un surfaçage radiculaire ?",
  "C'est le geste central du traitement non chirurgical de la parodontite : il retire la plaque et le tartre situés sous la gencive, avec un éventuel retrait d'une partie du cément de la racine."),
 ("Surfaçage et détartrage, est-ce la même chose ?",
  "Non. Le retrait professionnel de la plaque et du tartre au-dessus de la gencive relève de la première étape du traitement. Le surfaçage agit sous la gencive, à l'étape suivante."),
 ("Le surfaçage se fait-il à la main ou aux ultrasons ?",
  "Les deux sont recommandés : instruments manuels, soniques ou ultrasoniques, ou une combinaison des deux."),
 ("Le laser est-il recommandé en complément du surfaçage ?",
  "Les recommandations européennes de 2020 suggèrent de ne pas utiliser les lasers ni la thérapie photodynamique en complément. « Non suggéré » ne signifie pas « dangereux » : les preuves ne montrent pas de bénéfice suffisant."),
 ("Faut-il des antibiotiques avec le surfaçage ?",
  "Pas en routine. Les antibiotiques par voie générale ne sont pas recommandés en routine, et la HAS recommande de ne pas utiliser d'antibiotique appliqué localement en pratique bucco-dentaire."),
 ("Que se passe-t-il après le surfaçage ?",
  "Une réévaluation a lieu à la fin de l'étape. Si les objectifs sont atteints, on passe aux soins de soutien. Sinon, une étape complémentaire est envisagée pour les sites qui n'ont pas répondu."),
],
claims_more=[
 ("Détartrage supragingival (étape 1) et surfaçage sous-gingival (étape 2).","S3_2020_FIG","Étapes 1 et 2"),
 ("Antibioprophylaxie du surfaçage non recommandée en population générale ; au cas par cas si risque infectieux augmenté.","HAS_ATB_2026","PDF, tableau 2, p. 13"),
],
)

# ------------------------------------------------------------------ 6
ENRICH_1["parodontite-et-diabete-un-lien-dans-les-deux-sens"] = dict(
seo_title="Parodontite et diabète : le lien",
meta="Diabète et maladies des gencives s'influencent. Ce que disent le consensus FID-EFP et la revue Cochrane sur l'effet du traitement des gencives sur l'HbA1c.",
figs={
"_intro": bidirectional("Un diabète mal contrôlé", "Une parodontite plus fréquente et plus grave",
  "Le lien décrit par le consensus fonctionne dans les deux sens : la parodontite est aussi associée à un risque accru de dérèglement de la glycémie.", label="Diabète et parodontite"),
"traitement": bars([
 ("À 3-4 mois", 0.43, " (preuve modérée)"),
 ("À 6 mois", 0.30, " (12 études)"),
 ("À 12 mois", 0.50, " (une seule étude)"),
], 0.6, " point", "Baisse moyenne de l'HbA1c après traitement parodontal, en points de pourcentage (revue Cochrane de 2022, 35 essais). À 12 mois, une seule étude est disponible : les effets à plus long terme restent à confirmer.", label="Baisse de l'HbA1c après traitement parodontal"),
},
more=[
("hba1c", "Que signifie une baisse de 0,4 point d'HbA1c ?",
 """<p>L'HbA1c reflète la glycémie moyenne des trois derniers mois. Une baisse de 0,4 point de pourcentage correspond, par exemple, à une valeur qui passerait de 8,0 % à environ 7,6 %. Les revues d'études décrivent un effet moyen : il varie d'une personne à l'autre. Il ne remplace pas le traitement du diabète, et vous ne devez jamais modifier votre traitement sans l'avis de votre médecin.</p>"""),
("quoi-faire", "Si vous êtes diabétique : trois réflexes",
 """<ul class="check-list">
<li>Faire contrôler vos gencives au moins une fois par an, même sans symptôme.</li>
<li>Informer votre dentiste de votre diabète, de votre traitement et de vos derniers résultats d'HbA1c.</li>
<li>Tenir votre médecin au courant des soins dentaires. Votre dentiste peut vous demander un résultat d'HbA1c de moins de 3 mois avant certains soins.</li>
</ul>"""),
],
gloss=[
 ("HbA1c", "Hémoglobine glyquée : reflet de la glycémie moyenne sur environ trois mois."),
 ("Hyperglycémie", "Taux de sucre dans le sang trop élevé."),
 ("Résistance à l'insuline", "Situation où l'organisme répond moins bien à l'insuline, hormone qui régule la glycémie."),
 ("Consensus", "Texte élaboré par des experts qui font la synthèse des données disponibles."),
 ("Revue Cochrane", "Synthèse méthodique d'essais cliniques réalisée selon des règles strictes."),
],
ask=[
 "Mon diabète change-t-il la façon dont mes gencives seront suivies ?",
 "Avez-vous besoin d'un résultat récent d'HbA1c avant ce soin ?",
 "Dois-je informer mon médecin de ce traitement des gencives ?",
 "À quelle fréquence dois-je faire contrôler mes gencives ?",
],
faq=[
 ("Le diabète favorise-t-il les maladies des gencives ?",
  "Selon le consensus de la Fédération internationale du diabète et de la Fédération européenne de parodontologie, une glycémie mal contrôlée est associée à un risque accru et à une gravité plus élevée de parodontite."),
 ("La parodontite peut-elle déséquilibrer le diabète ?",
  "Les personnes atteintes de parodontite ont un risque accru de dérèglement de la glycémie, de résistance à l'insuline et de diabète de type 2. Ces données décrivent des associations observées dans les études."),
 ("Traiter les gencives fait-il baisser la glycémie ?",
  "Dans les études analysées, le traitement parodontal s'accompagne d'une baisse moyenne de l'HbA1c : 0,27 à 0,48 point selon le consensus de 2018, environ 0,4 point à 3-4 mois selon la revue Cochrane de 2022, avec un niveau de preuve modéré."),
 ("Le traitement des gencives remplace-t-il le traitement du diabète ?",
  "Non. Il peut s'ajouter à une bonne prise en charge globale, en lien avec le médecin. Ne modifiez jamais votre traitement sans son avis."),
 ("Le traitement parodontal est-il sûr chez une personne diabétique ?",
  "Il n'a pas montré de problème de sécurité particulier, mais les effets indésirables ont été peu étudiés. Informez votre dentiste de votre diabète et de vos derniers résultats d'HbA1c."),
 ("Dois-je prévenir mon dentiste que je suis diabétique ?",
  "Oui, avec votre traitement et vos derniers résultats d'HbA1c. Il peut vous demander un résultat de moins de 3 mois avant certains soins."),
],
claims_more=[
 ("Exemple chiffré : de 8,0 % à environ 7,6 % (illustration arithmétique d'une baisse de 0,4 point).","SIMPSON_2022","Illustration, pas un résultat d'étude"),
],
)

# ------------------------------------------------------------------ 7
ENRICH_1["parodontite-et-sante-du-coeur-consensus-europeen"] = dict(
seo_title="Parodontite et santé du cœur",
meta="Parodontite sévère et maladies cardiovasculaires : ce qui est établi, ce qui ne l'est pas et ce que le consensus EFP et Fédération mondiale du cœur conseille.",
figs={
"anticoagulants": flow([
 ("Informer votre dentiste", "Votre état cardiovasculaire, vos traitements et tout traitement anticoagulant."),
 ("Ne rien modifier de vous-même", "Seuls le chirurgien-dentiste et le médecin qui prescrit le traitement peuvent décider de l'adapter."),
 ("Des mesures locales", "La plupart des actes à faible risque hémorragique se font sans interrompre le traitement, avec des mesures locales."),
 ("Un avis médical en cas de doute", "Le chirurgien-dentiste prend l'avis du médecin ou du cardiologue."),
], "Anticoagulants et antiplaquettaires : la conduite décrite par le consensus.", label="Anticoagulants et soins dentaires"),
"_intro": cards([
 ("Établi : une association", "Les preuves épidémiologiques d'une association entre parodontite sévère et maladies cardiovasculaires sont solides."),
 ("Preuves modérées : des marqueurs", "Baisse de marqueurs de l'inflammation (CRP, interleukine 6) et meilleure fonction des parois des vaisseaux après traitement. Pas d'effet sur les lipides."),
 ("Preuves insuffisantes : la prévention", "On ne peut pas affirmer que traiter les gencives prévient ou retarde les accidents cardiovasculaires."),
], "Trois niveaux de connaissance, selon le consensus de 2020. Associé ne veut pas dire cause.", label="Niveaux de preuve"),
},
more=[
("securite", "Le traitement des gencives est-il sans danger pour le cœur ?",
 """<p>Selon le consensus, le traitement parodontal ne semble pas augmenter le risque cardiovasculaire ischémique. Un traitement de toute la bouche réalisé en 24 heures provoque en revanche une inflammation générale transitoire : c'est une raison de plus d'informer votre dentiste de votre état cardiovasculaire et de vos traitements.</p>"""),
],
gloss=[
 ("Association", "Lien statistique observé dans des études. Il ne prouve pas qu'une maladie en cause une autre."),
 ("Athérome", "Dépôt qui épaissit la paroi des artères. Des bactéries de la bouche ont été retrouvées dans des plaques d'athérome."),
 ("CRP et interleukine 6", "Substances du sang dont le taux augmente en cas d'inflammation."),
 ("Fonction endothéliale", "Capacité des parois des vaisseaux à se dilater et à se contracter normalement."),
 ("Antiplaquettaire, anticoagulant", "Médicaments qui limitent la formation de caillots. Seuls le chirurgien-dentiste et le médecin qui les prescrit peuvent décider de les adapter."),
],
ask=[
 "Mon état cardiaque ou mes médicaments changent-ils la façon dont vous me soignez ?",
 "Faut-il que vous contactiez mon médecin ou mon cardiologue avant ce soin ?",
 "Le traitement de toute la bouche en une séance est-il adapté à ma situation ?",
],
faq=[
 ("Les maladies des gencives peuvent-elles provoquer un infarctus ?",
  "Le consensus conclut à une association entre parodontite sévère et maladies cardiovasculaires (maladie coronarienne, accident vasculaire cérébral, artériopathie périphérique, fibrillation auriculaire, insuffisance cardiaque). Associé ne veut pas dire cause : ce sont des liens statistiques observés dans des études."),
 ("Soigner ses gencives protège-t-il le cœur ?",
  "Les preuves sont insuffisantes pour affirmer que le traitement parodontal prévient ou retarde les accidents cardiovasculaires. Soigner ses gencives reste utile en soi."),
 ("Le traitement parodontal est-il risqué quand on a une maladie du cœur ?",
  "Il ne semble pas augmenter le risque cardiovasculaire ischémique. Un traitement de toute la bouche en 24 heures provoque une inflammation générale transitoire."),
 ("Dois-je arrêter mes anticoagulants avant un soin des gencives ?",
  "Non, pas de votre propre initiative. Selon le consensus, la plupart des actes à faible risque hémorragique peuvent être réalisés sans interrompre ces médicaments, avec des mesures locales. Votre dentiste décide avec votre médecin."),
 ("Que dois-je dire à mon dentiste ?",
  "Votre état cardiovasculaire, vos traitements et tout traitement anticoagulant ou antiplaquettaire."),
],
claims_more=[
 ("Association avec maladie coronarienne, AVC, artériopathie périphérique, fibrillation auriculaire, insuffisance cardiaque.","SANZ_CVD_2020","Conclusions, épidémiologie"),
 ("Inflammation systémique transitoire après traitement bouche entière en 24 h ; pas de sur-risque ischémique.","SANZ_CVD_2020","Conclusions, sécurité"),
],
)
