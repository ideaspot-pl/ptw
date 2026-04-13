<?php

$recipes = [
    'Pancakes' => [
        'Flour' => ['qty' => 200, 'unit' => 'g'],
        'Milk'  => ['qty' => 300, 'unit' => 'ml'],
        'Eggs'  => ['qty' => 2, 'unit' => 'pcs'],
    ],
    'Guacamole' => [
        'Avocado' => ['qty' => 2, 'unit' => 'pcs'],
        'Lime'    => ['qty' => 1, 'unit' => 'pcs'],
        'Salt'    => ['qty' => 1, 'unit' => 'tsp'],
    ],
];

echo "<pre>";
foreach ($recipes as $recipeName => $ingredients) {
    echo $recipeName . ":\n";
    foreach ($ingredients as $ingredientName => $meta) {
        echo "  - {$ingredientName}: {$meta['qty']} {$meta['unit']}\n";
    }
    echo "\n";
}
echo "</pre>";
