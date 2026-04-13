<?php

require_once __DIR__ . '/../config.php';
global $config;

$pdo = new PDO($config['dsn'], $config['username'], $config['password']);
$sql = 'SELECT * FROM user WHERE id >= :min AND id <= :max';
$statement = $pdo->prepare($sql);


$result = $statement->execute(array(
    'min' => 0,
    'max' => 10,
));

while ($row = $statement->fetch()) {
    var_dump($row);
}
