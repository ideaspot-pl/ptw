<?php

$userAgent = 'Mozilla/5.0 (iPhone Simulator; U;
    CPU iPhone OS 4_3_2 like Mac OD X; en-us)
       AppleWebKit/535.17.9 (KHTML, like Gecko) Version/5.0.2
       Mobile/8H7 Safari/6533.18.5';

$url = 'https://api.github.com/repos/ideaspot-pl/ptw/commits?per_page=3';

$ch = curl_init($url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_USERAGENT, $userAgent);

$response = curl_exec($ch);
$httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);

if (!$response || $httpCode !== 200) {
    die("No response.");
}
var_dump($response);

$json = json_decode($response);
var_dump($json);
