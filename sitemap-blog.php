<?php
// Plan du site du blog : ne liste que les articles dont la date de publication est atteinte.
// Genere par blog-interne/_outils/generer_blog.py. Reference dans robots.txt.
header('Content-Type: application/xml; charset=utf-8');
date_default_timezone_set('Europe/Paris');
$today = date('Y-m-d');
$articles = [
  ['slug' => 'antibiotiques-chez-le-dentiste-ce-que-recommande-la-has', 'date' => '2026-11-05'],
  ['slug' => 'gencives-qui-saignent-la-gingivite', 'date' => '2026-11-16'],
  ['slug' => 'parodontite-comprendre-la-maladie-des-gencives', 'date' => '2026-11-23'],
  ['slug' => 'traiter-une-parodontite-les-quatre-etapes', 'date' => '2026-11-30'],
  ['slug' => 'le-surfacage-radiculaire-recommandations-europeennes', 'date' => '2026-12-07'],
  ['slug' => 'parodontite-et-diabete-un-lien-dans-les-deux-sens', 'date' => '2026-12-14'],
  ['slug' => 'parodontite-et-sante-du-coeur-consensus-europeen', 'date' => '2026-12-21'],
  ['slug' => 'apres-le-traitement-parodontal-la-maintenance', 'date' => '2026-12-28'],
  ['slug' => 'implant-dentaire-le-parcours-evalue-par-la-has', 'date' => '2027-01-04'],
  ['slug' => 'implants-dentaires-survie-a-dix-ans-que-disent-les-etudes', 'date' => '2027-01-11'],
  ['slug' => 'peut-on-poser-un-implant-apres-une-parodontite', 'date' => '2027-01-18'],
  ['slug' => 'peri-implantite-reconnaitre-prevenir-traiter', 'date' => '2027-01-25'],
  ['slug' => 'prothese-sur-implant-vissee-ou-scellee', 'date' => '2027-02-01']
];
echo '<?xml version="1.0" encoding="UTF-8"?>' . "\n";
echo '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' . "\n";
foreach ($articles as $a) {
    if ($a['date'] <= $today) {
        echo '  <url><loc>https://www.dentiste-paris12.com/blog/' . $a['slug'] . '</loc><lastmod>' . $a['date'] . '</lastmod><changefreq>monthly</changefreq><priority>0.5</priority></url>' . "\n";
    }
}
echo '</urlset>' . "\n";
