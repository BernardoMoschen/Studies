<?php
require_once 'funcoes.php';

/*
List é uma forma elegante de pegar os valores de um array apra variáveis separadas.

=> Declaração:
    - Padrão: 
        list('titular' => $titular, 'saldo' => $saldo) = $conta;

    - Forma enxuta, semelhante a um array:
        ['titular' => $titular, 'saldo' => $saldo] = $conta;
*/

// Exemplo:
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

foreach ($contasCorrentes as $cpf => $conta) {
    ['titular' => $titular, 'saldo' => $saldo] = $conta;
    exibeMensagem(
        "$cpf $titular  $saldo"
    );
}