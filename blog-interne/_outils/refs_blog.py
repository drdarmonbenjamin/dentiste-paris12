# -*- coding: utf-8 -*-
"""Références bibliographiques du blog (parodontologie et implantologie).

Chaque entrée : clé -> (citation, url, statut de vérification).
Statut :
  "OK"  = référence lue sur une page officielle ou un dépôt institutionnel
          (lecture assistée par un outil de résumé), identité confirmée
          (auteurs, titre, revue, année, DOI).
  "A CONFIRMER" = un élément (volume, pages, année exacte) n'a pas pu être
          confirmé. Le relecteur scientifique doit le vérifier.
"""

REFS = {
    "S3_2020": (
        "Sanz M, Herrera D, Kebschull M, Chapple I, Jepsen S, Berglundh T, Sculean A, Tonetti MS. "
        "Treatment of stage I–III periodontitis: the EFP S3 level clinical practice guideline. "
        "<em>J Clin Periodontol</em>. 2020;47(Suppl 22):4-60. doi:10.1111/jcpe.13290",
        "https://doi.org/10.1111/jcpe.13290", "OK"),
    "S3_STADE4_2022": (
        "Fédération européenne de parodontologie (EFP). Treatment of stage IV periodontitis: the EFP S3 level clinical practice guideline. "
        "<em>J Clin Periodontol</em>. 2022;49(Suppl 24). doi:10.1111/jcpe.13639",
        "https://doi.org/10.1111/jcpe.13639", "OK (revue, année, volume et DOI confirmés sur la page de l'EFP ; auteurs et pages non repris)"),
    "S3_2020_FIG": (
        "Fédération européenne de parodontologie (EFP). Traitement de la parodontite de stades I à III : "
        "les quatre étapes (document de synthèse issu de la recommandation S3 de 2020).",
        "https://www.efp.org/fileadmin/uploads/efp/Photos/Continuing_Education/guidelineStagei-III4stepscombined.pdf", "OK"),
    "S3_PERI_2023": (
        "Herrera D, Berglundh T, Schwarz F, Chapple I, Jepsen S, Sculean A, Kebschull M, Papapanou PN, Tonetti MS, Sanz M. "
        "Prevention and treatment of peri-implant diseases: the EFP S3 level clinical practice guideline. "
        "<em>J Clin Periodontol</em>. 2023;50(Suppl 26):4-76. doi:10.1111/jcpe.13823",
        "https://doi.org/10.1111/jcpe.13823", "OK"),
    "EFP_PERI_INFO": (
        "Fédération européenne de parodontologie (EFP). Guideline on treatment of peri-implant diseases "
        "(infographies issues de la recommandation S3 de 2023).",
        "https://www.efp.org/education/continuing-education/clinical-guidelines/guideline-on-treatment-of-peri-implant-diseases/", "OK"),
    "PAPA_2018": (
        "Papapanou PN, Sanz M, Buduneli N, et al. Periodontitis: consensus report of workgroup 2 of the 2017 "
        "World Workshop on the Classification of Periodontal and Peri-Implant Diseases and Conditions. "
        "<em>J Periodontol</em>. 2018;89(Suppl 1):S173-S182. doi:10.1002/JPER.17-0721",
        "https://doi.org/10.1002/JPER.17-0721", "OK"),
    "CHAPPLE_2018": (
        "Chapple ILC, Mealey BL, Van Dyke TE, et al. Periodontal health and gingival diseases and conditions on an "
        "intact and a reduced periodontium: consensus report of workgroup 1 of the 2017 World Workshop on the "
        "Classification of Periodontal and Peri-Implant Diseases and Conditions. "
        "<em>J Clin Periodontol</em>. 2018;45(Suppl 20):S68-S77. doi:10.1111/jcpe.12940",
        "https://doi.org/10.1111/jcpe.12940", "OK"),
    "BERG_2018": (
        "Berglundh T, Armitage G, Araujo MG, et al. Peri-implant diseases and conditions: consensus report of "
        "workgroup 4 of the 2017 World Workshop on the Classification of Periodontal and Peri-Implant Diseases and "
        "Conditions. <em>J Periodontol</em>. 2018;89(Suppl 1):S313-S318. doi:10.1002/JPER.17-0739",
        "https://doi.org/10.1002/JPER.17-0739", "OK (revue, volume et pages confirmés par Europe PMC ; texte intégral non ouvert, facteurs de risque recoupés avec Herrera 2023)"),
    "SANZ_DIAB_2018": (
        "Sanz M, Ceriello A, Buysschaert M, et al. Scientific evidence on the links between periodontal diseases and "
        "diabetes: consensus report and guidelines of the joint workshop on periodontal diseases and diabetes by the "
        "International Diabetes Federation and the European Federation of Periodontology. "
        "<em>J Clin Periodontol</em>. 2018;45(2):138-149. doi:10.1111/jcpe.12808",
        "https://doi.org/10.1111/jcpe.12808", "OK"),
    "SANZ_CVD_2020": (
        "Sanz M, Marco del Castillo A, Jepsen S, et al. Periodontitis and cardiovascular diseases: consensus report. "
        "<em>J Clin Periodontol</em>. 2020;47(3):268-288. doi:10.1111/jcpe.13189",
        "https://doi.org/10.1111/jcpe.13189", "OK"),
    "EFP_CARDIO": (
        "Fédération européenne de parodontologie (EFP). Perio &amp; Cardio : rapport de consensus scientifique "
        "(EFP et World Heart Federation).",
        "https://www.efp.org/for-patients/gum-disease-general-health/clinical-guidelines/scientific-report/", "OK"),
    "HOWE_2019": (
        "Howe MS, Keys W, Richards D. Long-term (10-year) dental implant survival: a systematic review and "
        "sensitivity meta-analysis. <em>J Dent</em>. 2019;84:9-21. doi:10.1016/j.jdent.2019.03.008",
        "https://doi.org/10.1016/j.jdent.2019.03.008", "OK"),
    "WITT_2014": (
        "Wittneben JG, Millen C, Brägger U. Clinical performance of screw- versus cement-retained fixed "
        "implant-supported reconstructions: a systematic review. "
        "<em>Int J Oral Maxillofac Implants</em>. 2014;29(Suppl):84-98 (conférence de consensus de l'ITI, 2013). doi:10.11607/jomi.2014suppl.g2.1",
        "https://doi.org/10.11607/jomi.2014suppl.g2.1", "OK"),
    "HAS_ATB_2026": (
        "Haute Autorité de santé (HAS). Prescription des antibiotiques en pratique bucco-dentaire. "
        "Recommandation de bonne pratique, validée le 16 juillet 2026, mise en ligne le 14 septembre 2026.",
        "https://www.has-sante.fr/jcms/p_3525810/fr/prescription-des-antibiotiques-en-pratique-bucco-dentaire", "OK"),
    "HAS_ATB_COMM": (
        "Haute Autorité de santé (HAS). En soins dentaires aussi, les antibiotiques ne sont pas automatiques. "
        "Communiqué du 14 septembre 2026.",
        "https://has-sante.fr/jcms/p_4423461/fr/en-soins-dentaires-aussi-les-antibiotiques-ne-sont-pas-automatiques", "OK"),
    "SIMPSON_2022": (
        "Simpson TC, et al. Treatment of periodontitis for glycaemic control in people with "
        "diabetes mellitus. <em>Cochrane Database Syst Rev</em>. 2022;4:CD004714. doi:10.1002/14651858.CD004714.pub4",
        "https://doi.org/10.1002/14651858.CD004714.pub4", "OK (résumé lu ; texte complet non ouvert)"),
    "ESPOSITO_2026": (
        "Esposito et al. Antibiotic prophylaxis for dental implant placement without bone augmentation. "
        "<em>Cochrane Database Syst Rev</em>. 2026;(9):CD004152. doi:10.1002/14651858.CD004152.pub5",
        "https://doi.org/10.1002/14651858.CD004152.pub5", "OK (résumé lu, publication du 1er septembre 2026 ; texte complet non ouvert)"),
    "HAS_IMPL_COMM": (
        "Haute Autorité de santé (HAS). Implants et prothèses dentaires : avis favorable de la HAS pour leur remboursement "
        "dans les édentements complet ou unitaire. Communiqué du 6 novembre 2024.",
        "https://has-sante.fr/jcms/p_3555021/fr/implants-et-protheses-dentaires-avis-favorable-de-la-has-pour-leur-remboursement-dans-les-edentements-complet-ou-unitaire", "OK"),
    "HAS_IMPL_2024": (
        "Haute Autorité de santé (HAS). Prise en charge implanto-prothétique de l’édentement. Évaluation des "
        "technologies de santé, avis du Collège du 17 octobre 2024, mise en ligne le 6 novembre 2024.",
        "https://www.has-sante.fr/jcms/p_3356489/fr/prise-en-charge-implanto-prothetique", "OK"),
    "AMELI_AGENESIES": (
        "Assurance Maladie (ameli). Agénésies dentaires multiples (enfant, adulte) : soins et prothèses dentaires pris en charge.",
        "https://www.ameli.fr/assure/remboursements/rembourse/soins-protheses-dentaires-optique-audition/consultations-soins-protheses-dentaires/agenesies-dentaires-multiples-enfant-adulte", "OK (page lue le 31 octobre 2026 ; à relire à la date de publication)"),
}
