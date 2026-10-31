# -*- coding: utf-8 -*-
"""Enrichissements des articles 8 à 13 : visuels, sections complémentaires, glossaire, questions fréquentes.

Chaque affirmation nouvelle reprend un contenu déjà sourcé dans l'article (voir claims_more).
"""
from visuels_blog import *

ENRICH_2 = {}

# ------------------------------------------------------------------ 8
ENRICH_2["apres-le-traitement-parodontal-la-maintenance"] = dict(
seo_title="Parodontite : la maintenance après soins",
meta="Après une parodontite, les soins de soutien limitent le risque de récidive : visites de 3 à 12 mois, brossettes interdentaires, arrêt du tabac.",
figs={
"pourquoi": loop([
 ("Le traitement actif atteint ses objectifs", "Plus de poche de plus de 4 mm avec saignement, plus de poche de 6 mm ou plus."),
 ("Visites de soutien, de 3 à 12 mois", "Le rythme dépend du profil de risque de chaque patient."),
 ("Hygiène personnalisée et retrait professionnel de routine", "Instructions adaptées, y compris pour le brossage entre les dents."),
], "Les soins de soutien forment un cycle sans fin : on ne « termine » pas une parodontite, on la maintient stable.", label="Cycle des soins de soutien"),
"domicile": verdict_table([
 ("Brossettes interdentaires, en complément du brossage", "oui", "Lorsque l'anatomie le permet."),
 ("Autres dispositifs interdentaires, là où la brossette ne passe pas", "sug", ""),
 ("Fil dentaire en premier choix", "nsug", "Il reste utile là où une brossette ne passe pas."),
 ("Brosse à dents électrique", "ouv", "Selon l'appréciation du praticien et du patient."),
 ("Dentifrices et bains de bouche antiseptiques", "cas", "Sur conseil du praticien, en complément du brossage, sans le remplacer."),
 ("Arrêt du tabac", "oui", ""),
 ("Contrôle du diabète", "sug", "À cette étape ; il était recommandé dès la première."),
 ("Activité physique et perte de poids", "inc", "L'effet sur la parodontite n'est pas établi."),
], "Soins de soutien : ce que recommande la Fédération européenne de parodontologie pour la maison et les facteurs de risque.", head=("Pratique", "Position"), label="Soins de soutien : hygiène et facteurs de risque"),
},
more=[
("entre-deux", "Entre deux visites : quand reprendre rendez-vous ?",
 """<p>Une personne traitée pour une parodontite garde un risque élevé de récidive. Chez elle, une inflammation de la gencive ne doit pas être considérée comme une simple gingivite. Sans attendre le prochain rendez-vous de suivi, consultez en cas de :</p>
<ul class="check-list">
<li>gencives rouges ou gonflées, ou saignements ;</li>
<li>dent qui bouge, ou espaces qui augmentent entre les dents ;</li>
<li>mauvaise haleine ou goût désagréable dans la bouche.</li>
</ul>
<p>Ces signes ne suffisent pas à poser un diagnostic, mais ils justifient un examen.</p>"""),
("adaptation", "Un suivi qui s'adapte à vous",
 """<p>Il n'existe pas de rythme unique : les recommandations parlent de visites « de 3 à 12 mois au maximum selon le profil de risque ». Le choix des brossettes (leur taille, leur nombre) dépend de l'anatomie de votre bouche, et la méthode de brossage se montre en bouche. C'est pourquoi les recommandations demandent des instructions d'hygiène personnalisées à chaque patient.</p>"""),
],
gloss=[
 ("Soins parodontaux de soutien", "Quatrième étape du traitement : visites régulières pour prévenir la récidive et la progression de la maladie."),
 ("Récidive", "Retour de la maladie après un traitement qui l'avait stabilisée."),
 ("Profil de risque", "Ensemble des éléments propres à chaque patient (tabac, diabète, historique de la maladie) qui déterminent le rythme des visites."),
 ("Brossette interdentaire", "Petite brosse conique ou cylindrique qui nettoie les espaces entre les dents."),
 ("Antiseptique", "Produit qui réduit les bactéries ; les bains de bouche et dentifrices antiseptiques ne remplacent pas le brossage."),
],
ask=[
 "À quel rythme dois-je revenir pour mes soins de soutien ?",
 "Quelles brossettes interdentaires conviennent à mes espaces, et comment les utiliser ?",
 "Un bain de bouche ou un dentifrice antiseptique est-il utile dans mon cas, et pour combien de temps ?",
 "Quels signes doivent me faire reprendre rendez-vous avant la prochaine visite ?",
],
faq=[
 ("Pourquoi faut-il un suivi après un traitement de parodontite ?",
  "Parce qu'un patient traité, même dont la maladie est stabilisée, garde un risque élevé de récidive. Les recommandations européennes de 2020 consacrent donc une étape entière, les soins de soutien, à prévenir la récidive et la progression de la maladie."),
 ("À quelle fréquence faut-il revenir ?",
  "Les visites sont espacées de 3 à 12 mois au maximum, selon le profil de risque de chacun. Votre praticien fixe le rythme qui vous convient."),
 ("Que se passe-t-il pendant une visite de soutien ?",
  "Les recommandations prévoient des instructions d'hygiène personnalisées, y compris pour le brossage entre les dents, et suggèrent un retrait professionnel de routine de la plaque et du tartre pour limiter la perte de dents."),
 ("Brossettes interdentaires ou fil dentaire ?",
  "Les brossettes interdentaires sont recommandées en complément du brossage, lorsque l'anatomie le permet. Le fil dentaire n'est pas suggéré en premier choix, mais il reste utile là où une brossette ne passe pas."),
 ("Une brosse à dents électrique est-elle meilleure ?",
  "Les recommandations laissent ce choix à l'appréciation du praticien et du patient."),
 ("Un bain de bouche antiseptique est-il nécessaire ?",
  "Il peut être envisagé dans certains cas, sur conseil du chirurgien-dentiste, en complément du brossage et du brossage entre les dents. Il ne les remplace pas, et la chlorhexidine en bain de bouche est prévue pour une durée limitée."),
 ("Le tabac a-t-il une importance après le traitement ?",
  "Oui : l'arrêt du tabac est recommandé à cette étape comme aux précédentes."),
],
claims_more=[
 ("Signes d'alerte entre deux visites (gencives rouges ou gonflées, saignements, dent qui bouge, espaces, haleine) : repris des articles 2, 3 et du consensus.","SANZ_CVD_2020","Recommandations pour les patients"),
 ("Boucle de la maintenance : critères d'entrée, visites de 3 à 12 mois, instructions personnalisées, détartrage de routine suggéré.","S3_2020_FIG","Étape 4"),
],
)

# ------------------------------------------------------------------ 9
ENRICH_2["implant-dentaire-le-parcours-evalue-par-la-has"] = dict(
seo_title="Implant dentaire : le parcours de la HAS",
meta="Trois phases, deux situations évaluées, un avis favorable au remboursement en 2024 : ce que la HAS dit du parcours de soins par implant dentaire.",
figs={
"evaluation": cards([
 ("Édentement complet", "Plus aucune dent sur l'arcade. Prothèse amovible complète retenue par des implants."),
 ("Édentement unitaire", "Une ou deux dents manquantes. Prothèse fixée sur un implant."),
], "Les deux situations évaluées par la HAS en 2024.", label="Édentement complet et unitaire"),
"parcours": flow([
 ("Avant le traitement", "Faisabilité (facteurs de risque généraux et locaux, étude préimplantaire), consentement éclairé, dossier médical, bouche assainie."),
 ("Le traitement", "Chirurgie de pose des implants, éventuels aménagements autour de l'implant, puis pose des prothèses."),
 ("Après le traitement", "Contrôles professionnels, actes préventifs à une fréquence adaptée aux facteurs de risque, hygiène quotidienne."),
], "Le parcours en trois phases décrit par la HAS.", label="Les trois phases du parcours"),
"remboursement": cards([
 ("L'avis de la HAS", "Évalue l'intérêt des prises en charge et s'est prononcée en 2024 de façon favorable au remboursement."),
 ("La décision de remboursement", "Relève de l'Assurance maladie et des pouvoirs publics, qui fixent les actes pris en charge et leurs tarifs."),
], "Un avis favorable n'est pas une décision de remboursement.", label="Avis et décision"),
},
more=[
("prerequis", "Pourquoi une bouche assainie avant la pose ?",
 """<p>Parmi les prérequis cités par la HAS : une bouche assainie, sans pathologie active, avec une bonne hygiène bucco-dentaire. C'est pourquoi une maladie des gencives doit être traitée avant d'envisager la pose. Voir l'article « Peut-on poser un implant après une parodontite ? ».</p>"""),
("devis", "Avant de vous décider",
 """<ul class="check-list">
<li>Vous avez le droit de recevoir un devis détaillé indiquant le prix de chaque acte et ce qui est pris en charge.</li>
<li>Le consentement éclairé fait partie de la phase qui précède le traitement : posez toutes vos questions avant de décider.</li>
<li>Renseignez-vous sur ameli.fr et auprès de votre organisme complémentaire pour savoir ce qui est remboursé aujourd'hui.</li>
</ul>"""),
],
gloss=[
 ("Édentement", "Absence d'une ou de plusieurs dents."),
 ("Prothèse supra-implantaire", "Prothèse (couronne, bridge ou prothèse amovible) qui repose sur un ou plusieurs implants."),
 ("Étude préimplantaire", "Bilan réalisé avant la pose pour évaluer la faisabilité du traitement."),
 ("Consentement éclairé", "Accord donné par le patient après avoir reçu une information claire sur le traitement, ses alternatives et ses risques."),
 ("Maintenance", "Suivi à long terme après la pose : contrôles professionnels et hygiène quotidienne."),
],
ask=[
 "Mon cas relève-t-il d'un édentement unitaire ou complet, et quelles options existent ?",
 "Quels examens et quelles étapes sont prévus avant la pose ?",
 "Ma bouche est-elle prête, ou y a-t-il des soins à faire d'abord ?",
 "Pouvez-vous me remettre un devis détaillé, acte par acte ?",
 "Quel suivi est prévu après la pose, et à quelle fréquence ?",
],
faq=[
 ("Qu'a évalué la HAS ?",
  "Les prises en charge implanto-prothétiques de l'édentement dans deux situations : l'édentement complet (prothèse amovible complète retenue par des implants) et l'édentement unitaire, c'est-à-dire une ou deux dents manquantes (prothèse fixée sur un implant)."),
 ("Quelles sont les trois phases du parcours ?",
  "Avant le traitement (faisabilité, consentement éclairé, bouche assainie), le traitement (pose des implants puis des prothèses), et la maintenance (contrôles professionnels, actes préventifs, hygiène quotidienne)."),
 ("Les implants sont-ils remboursés ?",
  "La HAS a rendu en 2024 un avis favorable au remboursement, mais cet avis n'est pas une décision de remboursement. Selon son communiqué, la pose d'implants n'est pas remboursée pour la majorité des patients. Consultez ameli.fr et votre organisme complémentaire."),
 ("Ai-je droit à un devis ?",
  "Oui. Avant tout traitement, vous avez le droit de recevoir un devis détaillé indiquant le prix de chaque acte et ce qui est pris en charge."),
 ("Pourquoi la HAS parle-t-elle de bouche assainie ?",
  "C'est un prérequis : une bouche sans pathologie active et avec une bonne hygiène bucco-dentaire doit précéder la pose."),
 ("Un suivi est-il nécessaire après la pose ?",
  "Oui. La HAS inclut dans le parcours une phase de maintenance, avec des séances de contrôle professionnel, des actes préventifs adaptés aux facteurs de risque du patient et une hygiène quotidienne."),
],
claims_more=[
 ("Cartes édentement complet / unitaire et phases : reprennent les contenus du corps de l'article.","HAS_IMPL_2024","Page HAS"),
 ("Distinction avis HAS / décision de remboursement : reprend le corps de l'article (avis d'octobre 2024).","HAS_IMPL_COMM","Communiqué du 6 novembre 2024"),
 ("Droit à un devis détaillé : reprend le corps de l'article.","AMELI_AGENESIES","Reprise du texte de l'article ; à revérifier à la date de publication"),
],
)

# ------------------------------------------------------------------ 10
ENRICH_2["implants-dentaires-survie-a-dix-ans-que-disent-les-etudes"] = dict(
seo_title="Implants : la survie à dix ans",
meta="Survie des implants à dix ans : 93,2 à 96,4 % selon la revue de 2019. Comment lire ces chiffres, leurs limites et ce qui influence la tenue d'un implant.",
figs={
"etude": interval_plot([
 dict(label="Méta-analyse classique", est=96.4, ci=(95.2, 97.5), pred=(91.5, 99.4)),
 dict(label="Analyse de sensibilité", est=93.2, ci=(90.1, 95.8), pred=(76.6, 100)),
], 75, 100, 5, " %", "Survie des implants à 10 ans (revue systématique de 2019). Le point est l'estimation, la barre épaisse l'intervalle de confiance à 95 %, la barre claire l'intervalle de prédiction (variation attendue d'une étude à l'autre).", label="Survie des implants à dix ans"),
"limites": cards([
 ("La survie de l'implant", "L'implant est-il encore en bouche après dix ans ? C'est ce que mesure l'étude."),
 ("La santé des tissus autour", "Gencive et os autour de l'implant sont-ils sains ? L'étude ne le mesure pas."),
], "Deux questions différentes : un implant en place peut avoir une complication.", label="Survie et santé des tissus"),
},
more=[
("lecture", "Comment lire un intervalle ?",
 """<ul class="check-list">
<li>L'<strong>intervalle de confiance à 95 %</strong> indique la marge d'incertitude autour de la moyenne calculée.</li>
<li>L'<strong>intervalle de prédiction</strong> indique la variation attendue d'une étude à une autre : plus il est large, plus les résultats diffèrent d'une étude à l'autre. Ici, il va de 91,5 % à 99,4 % dans l'analyse classique et de 76,6 % à 100 % dans l'analyse de sensibilité.</li>
<li>Aucun de ces chiffres n'est une promesse pour une personne donnée.</li>
</ul>"""),
("agir", "Ce que vous pouvez faire",
 """<p>La HAS inclut dans le parcours de soins une phase de maintenance : contrôles professionnels, actes préventifs et hygiène bucco-dentaire quotidienne. Le consensus de 2017 associe l'absence de maintenance régulière, un mauvais contrôle de la plaque et un antécédent de parodontite sévère à un risque accru de péri-implantite. Les rendez-vous de suivi font donc partie du traitement.</p>"""),
],
gloss=[
 ("Revue systématique", "Recherche méthodique de toutes les études sur une question, avec des critères de sélection fixés à l'avance."),
 ("Méta-analyse", "Calcul statistique qui combine les résultats de plusieurs études."),
 ("Survie implantaire", "Proportion d'implants encore en bouche à une date donnée. Elle ne dit rien de l'état des tissus autour."),
 ("Analyse de sensibilité", "Calcul refait avec d'autres hypothèses, ici pour tenir compte des données manquantes et des patients perdus de vue."),
 ("Péri-implantite", "Inflammation des tissus autour d'un implant, avec perte osseuse progressive."),
],
ask=[
 "Quels facteurs de ma situation peuvent influencer la tenue de mon implant ?",
 "Quel suivi professionnel est prévu après la pose, et à quelle fréquence ?",
 "Comment brosser autour de mon implant au quotidien ?",
],
faq=[
 ("Combien de temps dure un implant dentaire ?",
  "Les études citées ne mesurent pas une durée de vie : elles comptent la proportion d'implants encore en place après dix ans. Dans la revue de 2019, elle est estimée à 96,4 % par la méta-analyse classique et à 93,2 % par l'analyse de sensibilité, que les auteurs présentent comme plus réaliste."),
 ("Un implant peut-il être perdu ?",
  "Oui : ces pourcentages, inférieurs à 100 %, signifient qu'une partie des implants est perdue. Les résultats varient nettement d'une étude à l'autre, et ils ne permettent pas de prévoir ce qui se passera pour une personne donnée."),
 ("Survie de l'implant et absence de complication, est-ce la même chose ?",
  "Non. La survie indique que l'implant est encore en bouche, pas que les tissus qui l'entourent sont en bonne santé."),
 ("Ces chiffres valent-ils pour tous les implants ?",
  "Non. Ils concernent des implants à vis à surface rugueuse, chez des adultes de 18 ans et plus, suivis pendant dix ans. Ils ne disent rien d'autres types d'implants ni de durées plus longues."),
 ("L'âge change-t-il les résultats ?",
  "Dans l'analyse de sensibilité, les auteurs relèvent un risque de perte d'implant possiblement plus élevé chez les patients de 65 ans et plus. Ce résultat vient d'études observationnelles et ne permet pas de prévoir ce qui se passera pour une personne donnée."),
 ("Qu'est-ce qui augmente le risque de complication autour d'un implant ?",
  "Selon le consensus mondial de 2017 : un antécédent de parodontite sévère, un mauvais contrôle de la plaque et l'absence de maintenance régulière après le traitement augmentent le risque de péri-implantite."),
],
claims_more=[
 ("Définitions du glossaire (revue systématique, méta-analyse, analyse de sensibilité, intervalle de prédiction) : explications méthodologiques générales, valeurs numériques reprises du corps de l'article.","HOWE_2019","Résumé"),
 ("Maintenance dans le parcours HAS ; facteurs associés à la péri-implantite.","HAS_IMPL_2024","Page HAS"),
],
)

# ------------------------------------------------------------------ 11
ENRICH_2["peut-on-poser-un-implant-apres-une-parodontite"] = dict(
seo_title="Implant après une parodontite ?",
meta="Un implant est-il possible après une parodontite ? Les recommandations européennes de 2023 demandent de traiter, stabiliser et suivre avant la pose.",
figs={
"recommandation": flow([
 ("Évaluer le profil de risque", "Repérer les facteurs que l'on peut modifier."),
 ("Traiter la gingivite et la parodontite", "Jusqu'à obtenir un état stable, selon les recommandations de traitement."),
 ("S'engager dans un programme de soins de soutien", "L'adhésion du patient est demandée avant la pose."),
 ("Envisager la pose", "La décision se prend au cas par cas, après examen."),
], "Ce que demande la recommandation européenne de 2023, avant la pose d'un implant.", label="Avant la pose : quatre étapes"),
"risque": verdict_table([
 ("Antécédent de parodontite sévère", "assoc", "Pour la péri-implantite."),
 ("Mauvais contrôle de la plaque", "assoc", "Pour la péri-implantite."),
 ("Absence de maintenance régulière après le traitement", "assoc", "Pour la péri-implantite."),
 ("Tabac", "moins", "Aide à l'arrêt tout de même recommandée par l'EFP en 2023."),
 ("Diabète", "moins", "Un bon contrôle de la glycémie est recommandé par l'EFP en 2023."),
 ("Bruxisme (serrer ou grincer des dents)", "inc", "On ne sait pas si le contrôler réduit le risque."),
], "Facteurs examinés avant et après la pose d'un implant (consensus mondial de 2017 et recommandation européenne de 2023).", head=("Facteur", "Ce que disent les experts"), label="Facteurs de risque autour d'un implant"),
},
more=[
("niveau", "Que signifie « preuve très faible, recommandation forte » ?",
 """<p>Cela peut sembler contradictoire. La recommandation est de grade A, c'est-à-dire forte, alors que son niveau de preuve est très faible : elle repose sur l'avis d'experts, avec un consensus unanime. Cette précision est donnée pour que vous sachiez ce qui est solide et ce qui l'est moins.</p>"""),
],
gloss=[
 ("Péri-implantite", "Inflammation des tissus autour d'un implant, avec perte osseuse progressive."),
 ("État stable", "Situation où la maladie des gencives est contrôlée à l'issue du traitement."),
 ("Soins de soutien", "Visites régulières de suivi après le traitement des gencives, pour prévenir la récidive."),
 ("Bruxisme", "Habitude de serrer ou de grincer des dents."),
 ("Grade A, preuve très faible", "Recommandation forte, fondée sur l'avis d'experts plutôt que sur des essais cliniques."),
],
ask=[
 "Mes gencives sont-elles dans un état stable, et que faut-il faire avant d'envisager un implant ?",
 "Quel suivi régulier devrai-je suivre avant et après la pose ?",
 "Mon tabac ou mon diabète influencent-ils mon projet, et comment être aidé ?",
 "Quelles alternatives à l'implant existent dans ma situation ?",
],
faq=[
 ("Peut-on poser un implant après une parodontite ?",
  "C'est possible à condition que la maladie soit traitée et stabilisée et qu'un suivi régulier soit en place. La décision se prend au cas par cas, après examen."),
 ("Pourquoi traiter les gencives avant la pose ?",
  "Parce qu'un antécédent de parodontite sévère figure parmi les facteurs associés à un risque accru de péri-implantite. La HAS demande aussi une bouche assainie, sans pathologie active, avant la pose."),
 ("Qu'est-ce que la péri-implantite ?",
  "C'est l'inflammation des tissus autour d'un implant, avec une perte osseuse progressive. Elle est détaillée dans l'article « Péri-implantite : reconnaître, prévenir, traiter »."),
 ("Le tabac et le diabète empêchent-ils d'avoir un implant ?",
  "Ce n'est pas ce que disent les recommandations : les données sur le tabac et le diabète sont moins tranchées que pour la plaque, mais l'EFP recommande l'aide à l'arrêt du tabac et, chez les personnes diabétiques, un bon contrôle de la glycémie."),
 ("Pourquoi un suivi avant même la pose ?",
  "Les recommandations demandent l'adhésion du patient à un programme de soins de soutien avant la pose, car l'absence de maintenance régulière est associée à un risque accru de péri-implantite."),
 ("Le bruxisme est-il un problème pour les implants ?",
  "Les recommandations européennes l'ont examiné, mais on ne sait pas aujourd'hui si le contrôler réduit le risque de maladie autour des implants."),
],
claims_more=[
 ("Précision sur le niveau de preuve (grade A, preuve très faible, avis d'experts, consensus unanime) : reprend le corps de l'article.","S3_PERI_2023","R5.1"),
 ("Tableau des facteurs : tabac et diabète moins tranchés ; aides recommandées ; bruxisme incertain.","BERG_2018","Facteurs de risque"),
],
)

# ------------------------------------------------------------------ 12
ENRICH_2["peri-implantite-reconnaitre-prevenir-traiter"] = dict(
seo_title="Péri-implantite : signes et traitements",
meta="Mucosite et péri-implantite : signes, prévention et traitements recommandés en 2023 par l'EFP, et position de la HAS sur les antibiotiques en 2026.",
figs={
"definitions": implant_triptych([
 ("sain", "<strong>Implant sain</strong><br>Pas de saignement, ni de suppuration, ni de perte osseuse au-delà du remodelage initial."),
 ("mucosite", "<strong>Mucosite</strong><br>Gencive enflammée qui saigne ou suppure, sans perte osseuse au-delà du remodelage initial."),
 ("perimplantite", "<strong>Péri-implantite</strong><br>Inflammation avec perte osseuse progressive autour de l'implant."),
], "Schémas simplifiés d'un implant dans la gencive et l'os.", label="Implant sain, mucosite et péri-implantite"),
"_prev": bars([
 ("Mucosite", 43, " (intervalle de confiance : 32 à 54 %)"),
 ("Péri-implantite", 22, " (intervalle de confiance : 14 à 30 %)"),
], 100, " %", "Pourcentage de patients porteurs d'implants concernés, selon une revue citée par la recommandation européenne. Les chiffres varient d'une étude à l'autre.", label="Fréquence de la mucosite et de la péri-implantite"),
"traitement": flow([
 ("Étape non chirurgicale", "Apprentissage de l'hygiène, contrôle des facteurs de risque, modification ou retrait de la prothèse si elle empêche le brossage, retrait professionnel de la plaque et du tartre sous la gencive."),
 ("Réévaluation à 6 à 12 semaines", "On vérifie si l'objectif est atteint."),
 ("Chirurgie si l'objectif n'est pas atteint", "À condition que l'hygiène du patient soit suffisante et, de préférence, par un praticien formé."),
 ("Suivi rapproché", "Après le traitement."),
], "Le traitement séquentiel de la péri-implantite (recommandation européenne de 2023).", label="Traitement de la péri-implantite"),
},
more=[
("signes", "Les signes à surveiller",
 """<p>Selon les définitions du consensus, une inflammation autour d'un implant se manifeste par un saignement et/ou une suppuration (du pus) au sondage, parfois une rougeur et un gonflement. Dans la péri-implantite, la profondeur de sondage augmente et la gencive peut se rétracter. La perte osseuse ne se voit pas à l'œil nu : elle se contrôle sur une radiographie, d'où l'intérêt de la radiographie de référence. Seul un examen permet de faire la différence : consultez dès l'apparition de signes inhabituels autour d'un implant.</p>"""),
("tableau-ttt", "Traitements : ce qui est recommandé et ce qui ne l'est pas",
 verdict_table([
  ("Hygiène personnelle et retrait professionnel de la plaque (mucosite)", "oui", "Contrôle 2 à 3 mois plus tard."),
  ("Antibiotique, local ou général (mucosite)", "non", ""),
  ("Étape non chirurgicale (péri-implantite)", "oui", "Réévaluation à 6 à 12 semaines."),
  ("Chirurgie (péri-implantite, si l'objectif n'est pas atteint)", "oui", "Hygiène suffisante ; praticien formé de préférence."),
  ("Antibiotique (péri-implantite)", "non", "Sauf cas particuliers selon la HAS (2026)."),
  ("Lasers, thérapie photodynamique, aéropolissage, gels, antimicrobiens locaux en complément", "nsug", ""),
 ], "Synthèse des recommandations européennes de 2023 et de la HAS de 2026.", head=("Pratique", "Position"), label="Traitements de la mucosite et de la péri-implantite")),
],
gloss=[
 ("Mucosite péri-implantaire", "Inflammation de la gencive autour d'un implant, sans perte osseuse au-delà du remodelage initial."),
 ("Péri-implantite", "Inflammation avec perte osseuse progressive autour d'un implant."),
 ("Suppuration", "Écoulement de pus."),
 ("Remodelage osseux initial", "Modification de l'os qui suit normalement la pose d'un implant."),
 ("Radiographie de référence", "Radiographie réalisée une fois le remodelage osseux terminé, pour pouvoir comparer ensuite."),
],
ask=[
 "Mes implants sont-ils sains ? Sondez-vous les tissus autour à chaque examen ?",
 "Dispose-t-on d'une radiographie de référence de mes implants ?",
 "Ma prothèse me permet-elle de brosser correctement autour de l'implant ?",
 "Si une inflammation apparaît, quel traitement envisagez-vous en premier ?",
],
faq=[
 ("Quelle différence entre mucosite et péri-implantite ?",
  "Dans la mucosite, la gencive autour de l'implant est enflammée sans perte osseuse au-delà du remodelage initial. Dans la péri-implantite, l'inflammation s'accompagne d'une perte osseuse progressive."),
 ("Quels sont les signes d'une péri-implantite ?",
  "Saignement et/ou suppuration au sondage, profondeur de sondage qui augmente, parfois récession de la gencive. Seul un examen permet de faire la différence avec une mucosite."),
 ("Est-ce fréquent ?",
  "Selon une revue citée par la recommandation européenne, la mucosite concernerait environ 4 patients porteurs d'implants sur 10 et la péri-implantite environ 2 sur 10. Ces chiffres varient d'une étude à l'autre."),
 ("Comment prévenir la péri-implantite ?",
  "La prévention commence avant la pose (traiter les gencives, évaluer le profil de risque), se poursuit à la conception de la prothèse (accès pour l'hygiène et pour la sonde) et après la mise en fonction (sondage à chaque examen, radiographie de référence)."),
 ("Faut-il un antibiotique ?",
  "Pas en routine. La recommandation européenne de 2023 ne le recommande pas pour la mucosite. Pour la péri-implantite, la HAS (2026) ne le recommande pas, sauf cas particuliers : patients à risque infectieux augmenté, signes d'extension de l'infection ou geste local impossible."),
 ("La péri-implantite se guérit-elle ?",
  "Le traitement ne réussit pas dans tous les cas : dans les essais, la résolution complète variait de 0 à 65 % selon les groupes. Le premier objectif est de conserver l'implant et sa prothèse lorsque c'est acceptable."),
 ("Peut-on garder son implant ?",
  "Dans les cas avancés, la décision de conserver ou de retirer l'implant appartient au praticien, après examen."),
],
claims_more=[
 ("Pourcentages 43 % et 22 % et leurs intervalles (illustration chiffrée).","S3_PERI_2023","Introduction (revue de Derks et Tomasi 2015)"),
 ("Radiographie de référence ; sondage à chaque examen ; signes cliniques.","BERG_2018","Définitions ; S3_PERI_2023 R5.1 à R5.4"),
 ("Tableau des traitements : reprend les recommandations R7 et R8 déjà sourcées dans le corps de l'article.","S3_PERI_2023","R7 et R8"),
],
)

ENRICH_2["peri-implantite-reconnaitre-prevenir-traiter"]["figs"]["definitions"] += ENRICH_2["peri-implantite-reconnaitre-prevenir-traiter"]["figs"].pop("_prev")

# ------------------------------------------------------------------ 13
ENRICH_2["prothese-sur-implant-vissee-ou-scellee"] = dict(
seo_title="Prothèse sur implant : vissée ou scellée",
meta="Prothèse sur implant vissée ou scellée : survie comparable à 5 ans, complications différentes. Ce que disent la revue de 2014 et le consensus de l'ITI.",
figs={
"principe": retention_pair("Deux façons de fixer une couronne sur un implant (schémas simplifiés)."),
"etude": bars([
 ("Scellée, à 5 ans", 96.03, ""),
 ("Vissée, à 5 ans", 95.55, " (différence non significative)"),
 ("Scellée, à 10 ans", 92.22, ""),
 ("Vissée, à 10 ans", 91.30, ""),
], 100, " %", "Survie des restaurations fixes sur implants (revue de 2014) : les deux modes de fixation donnent des résultats comparables.", label="Survie des prothèses scellées et vissées"),
},
more=[
("comparer", "Avantages et limites de chaque mode",
 cards([
  ("Prothèse scellée", "Moins d'éclats de la céramique. Mais perte de rétention plus fréquente, complications biologiques et fistules plus fréquentes, et élimination incomplète du ciment considérée comme un inconvénient majeur."),
  ("Prothèse vissée", "Complications techniques moins fréquentes au total (7,50 contre 9,81 événements pour 100 ans), possibilité d'intervenir après la pose. Mais éclats de céramique plus fréquents, desserrage de la vis et perte du bouchon de l'orifice, positionnement précis de l'implant exigé."),
 ], "Comparaison issue de la revue systématique de 2014.", label="Scellée et vissée : avantages et limites")),
("suivi", "Si vous avez une prothèse sur implant",
 """<p>Quel que soit le mode de fixation, la prévention de la péri-implantite repose sur un accès suffisant pour l'hygiène et un suivi régulier (voir l'article « Péri-implantite : reconnaître, prévenir, traiter »). Si une prothèse vissée se desserre ou si l'orifice de la vis n'est plus refermé, ces événements, propres aux prothèses vissées, doivent être examinés par votre praticien.</p>"""),
],
gloss=[
 ("Pilier implantaire", "Pièce qui relie l'implant à la prothèse."),
 ("Prothèse scellée", "Prothèse fixée sur le pilier avec un ciment."),
 ("Prothèse vissée (transvissée)", "Prothèse fixée par une vis, accessible par un petit orifice que l'on referme ensuite."),
 ("Ciment résiduel", "Excès de ciment resté sous la gencive après le scellement. Les auteurs de la revue l'associent aux maladies péri-implantaires."),
 ("Consensus de l'ITI", "Texte de la conférence de consensus de l'International Team for Implantology (2013), issu de la revue systématique."),
],
ask=[
 "Mon traitement sera-t-il vissé ou scellé, et pourquoi dans mon cas ?",
 "Comment ferez-vous pour qu'aucun excès de ciment ne reste sous la gencive ?",
 "Si ma prothèse est vissée, comment sera refermé l'orifice de la vis ?",
 "Pourrez-vous intervenir facilement sur la prothèse si nécessaire ?",
],
faq=[
 ("Prothèse vissée ou scellée : laquelle choisir ?",
  "La survie à 5 ans est comparable (96,03 % pour les scellées, 95,55 % pour les vissées). Les auteurs de la revue suggèrent de privilégier la rétention vissée, mais le consensus issu de cette revue précise qu'aucune recommandation universelle ne peut être faite : le choix relève du praticien, au cas par cas."),
 ("Le ciment peut-il poser problème ?",
  "La revue ne mesure pas le ciment en excès comme critère de résultat, mais ses auteurs considèrent l'élimination incomplète du ciment comme un inconvénient majeur du scellement. Le consensus mondial de 2017 le cite parmi les facteurs de risque de péri-implantite, avec des preuves jugées limitées."),
 ("Un praticien qui scelle une prothèse travaille-t-il moins bien ?",
  "Non : ce choix ne permet pas de juger la qualité d'un traitement. Un praticien qui choisit de sceller une prothèse peut avoir de bonnes raisons de le faire."),
 ("Quelles complications sont propres à la prothèse vissée ?",
  "Le desserrage de la vis et la perte du bouchon de l'orifice ne concernent que les prothèses vissées. Les éclats de la céramique y sont aussi plus fréquents."),
 ("Et pour une couronne sur un seul implant ?",
  "L'estimation de survie à 5 ans est plus basse avec les prothèses vissées (91,2 % contre 96,4 %), mais la différence n'est pas statistiquement significative et l'incertitude est large."),
 ("Ces données sont-elles récentes ?",
  "La revue porte sur des études publiées jusqu'en 2012 : les matériaux et les techniques ont évolué depuis. Les études incluses sont hétérogènes et il n'existe pas de définition standard de l'échec d'une prothèse."),
],
claims_more=[
 ("Cartes de comparaison : reprennent les résultats déjà sourcés dans le tableau de l'article (complications techniques 9,81 contre 7,50 pour 100 ans, éclats, perte de rétention, fistule).","WITT_2014","Résultats"),
 ("Possibilité d'intervenir après la pose (rétention vissée) : formulée comme contrepartie des « possibilités limitées d'intervenir après un scellement définitif ».","WITT_2014","Conclusions"),
 ("Glossaire : définition du consensus de l'ITI (2013) ; pilier = définition générale.","WITT_2014","Intitulé de la référence (conférence de consensus de l'ITI, 2013)"),
],
)
