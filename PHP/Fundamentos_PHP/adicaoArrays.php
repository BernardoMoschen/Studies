<?php

/* 
    Ao adicionarmos um item a um array, sem passar o índice, o PHP adiciona um índice número, ]
sempre selecioando o próximo número não usado disponível
*/

$listaIdades = [23, 19, 25, 30, 41, 18, 21];
// índices =     0,  1,  2,  3,  4,  5,  6

$listaIdades[] = 20; // Adiciona o valor 20 ao índice 7(último), pois não foi passado índice desejado

$contasCorrentes = [
    11111=> [
        'titular' => 'Bernardo', // Chave = 'titular', valor do índice = 'Bernardo'
        'saldo' => 1000 // Chave = 'saldo', valor do índice = '1000'
    ],
    11112 => [
        'titular' => 'Maria', // Chave = 'titular', valor do índice = 'Maria'
        'saldo' => 9875 // Chave = 'saldo', valor do índice = '9875'
    ],
    11113 => [
        'titular' => 'Adalberto', // Chave = 'titular', valor do índice = 'Adalberto'
        'saldo' => 4500 // Chave = 'saldo', valor do índice = '4500'
    ]
];

$contasCorrentes[] = [ // PHP adicionará o array ao índice '11114', pois é o próximo valor número disponível'
    'titular' => 'Claudiano',
    'saldo' => 555,
];

$contasCorrentes['22222'] = [ // Adiciona com o índice '22222'
    'titular' => 'Fui adiciona com um índice',
    'saldo' => 12345,
];

foreach($contasCorrentes as $cpf => $conta){ // Atribuindo o nome do índice a váriavel $cpf
    echo $cpf . PHP_EOL; // Acessando o índice
    echo $conta['titular'] . PHP_EOL; // Acessando a o índice titular
}
