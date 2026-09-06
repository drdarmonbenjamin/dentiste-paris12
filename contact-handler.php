<?php
/**
 * Traitement du formulaire de contact - hébergé directement chez OVH.
 * Aucune donnée ne transite par un prestataire tiers : tout reste sur ce serveur
 * et part directement par email depuis l'hébergement français du cabinet.
 * Compatible PHP 5.3+ (volontairement écrit en syntaxe ancienne pour compatibilité).
 */

header('Content-Type: application/json; charset=utf-8');

// --- Anti-spam (honeypot) : si ce champ caché est rempli, c'est un robot ---
if (!empty($_POST['botcheck'])) {
    echo json_encode(array('success' => true));
    exit;
}

// --- Nettoyage basique des champs (anti-injection d'en-têtes email) ---
function cd_clean($value) {
    $value = trim($value);
    $value = str_replace(array("\r", "\n", "%0a", "%0d"), ' ', $value);
    return $value;
}

$name    = isset($_POST['name'])    ? cd_clean($_POST['name'])    : '';
$email   = isset($_POST['email'])   ? cd_clean($_POST['email'])   : '';
$phone   = isset($_POST['phone'])   ? cd_clean($_POST['phone'])   : '';
$message = isset($_POST['message']) ? trim(str_replace(array("\r\n", "\r"), "\n", $_POST['message'])) : '';
$consent = isset($_POST['consent']) ? $_POST['consent'] : '';

// --- Validation minimale ---
if ($name === '' || $email === '' || $phone === '' || $consent === '' || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
    header('HTTP/1.1 400 Bad Request');
    echo json_encode(array('success' => false, 'message' => 'Merci de renseigner tous les champs obligatoires.'));
    exit;
}

$to      = 'drdarmonbenjamin@gmail.com';
$subject = 'Nouveau message depuis dentiste-paris12.com';

$body  = "Nouveau message recu via le formulaire de contact du site.\n\n";
$body .= "Nom : " . $name . "\n";
$body .= "Email : " . $email . "\n";
$body .= "Telephone : " . $phone . "\n";
$body .= "Message :\n" . ($message !== '' ? $message : '(aucun message)') . "\n";

$headers  = "From: noreply@dentiste-paris12.com\r\n";
$headers .= "Reply-To: " . $email . "\r\n";
$headers .= "Content-Type: text/plain; charset=UTF-8\r\n";

$sent = @mail($to, $subject, $body, $headers);

if ($sent) {
    echo json_encode(array('success' => true));
} else {
    header('HTTP/1.1 500 Internal Server Error');
    echo json_encode(array('success' => false, 'message' => "Une erreur est survenue lors de l'envoi."));
}
