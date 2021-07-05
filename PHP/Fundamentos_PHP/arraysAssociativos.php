<?php

/* Arrays associativos são a solução para quando precisamos 'nomear' um 
índice correspondente a um valor.
*/

// Declaração:
$conta001 = [
    'titular' => 'Bernardo', // Chave = 'titular', valor do índice = 'Bernardo'
    'saldo' => 1000 // Chave = 'saldo', valor do índice = '1000'
];

$conta002 = [
    'titular' => 'Maria', // Chave = 'titular', valor do índice = 'Maria'
    'saldo' => 9875 // Chave = 'saldo', valor do índice = '9875'
];  

$conta003 = [
    'titular' => 'Adalberto', // Chave = 'titular', valor do índice = 'Adalberto'
    'saldo' => 4500 // Chave = 'saldo', valor do índice = '4500'
];

// Array contendo as contas correntes:
$contasCorrentes = [$conta001, $conta002, $conta003];

// Acessando dados de um array associativo:
echo $conta001['titular'] . PHP_EOL; // = Bernardo

// Iterando em um array associativo:

for ($i = 0; $i < count($contasCorrentes); $i++){
    echo $contasCorrentes[$i]['titular'] . PHP_EOL;
}