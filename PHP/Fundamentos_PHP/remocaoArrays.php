<?php

/* 
Para remover um item de um índice usa-se a função 'unset':

=> Declaração:
    unset($seuArray['índice']);
*/

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

// Exemplo:

unset($contasCorrentes['11111']); // Remove o item de índice 11111 do array
foreach($contasCorrentes as $cpf => $conta){ // Atribuindo o nome do índice a váriavel $cpf
    echo $cpf . PHP_EOL; // Acessando o índice
    echo $conta['titular'] . PHP_EOL; // Acessando a o índice titular
}
