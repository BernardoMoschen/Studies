<?php 

// O loop forEach permite iterar sem iniciar um contador e sem saber o valor dos índices

$contasCorrentas = [
    123989812 => [
        'titular' => 'Bernardo', // Chave = 'titular', valor do índice = 'Bernardo'
        'saldo' => 1000 // Chave = 'saldo', valor do índice = '1000'
    ],
    12039801923 => [
        'titular' => 'Maria', // Chave = 'titular', valor do índice = 'Maria'
        'saldo' => 9875 // Chave = 'saldo', valor do índice = '9875'
    ],
    1238129321 => [
        'titular' => 'Adalberto', // Chave = 'titular', valor do índice = 'Adalberto'
        'saldo' => 4500 // Chave = 'saldo', valor do índice = '4500'
    ]
];

// Utiização do forEach
foreach ($contasCorrentas as $cpf => $conta){ // Atribuindo o nome do índice a váriavel $cpf
    echo $cpf . PHP_EOL; // Acessando o índice
    echo $conta['titular'] . PHP_EOL; // Acessando a o índice titular
}