<?php

/* 
Diferenças entre tipos de passagem de paramêtros:

    => Por VALOR: ocorre uma cópia dos valores e os mesmos são passados por parâmetro,
        ou seja, os valores originais não sofrem qualquer tipo de alteração.

    => Por REFERÊNCIA: ocorre uma passagem da refêrencia do valor original, portanto,
        qualquer modificação ocorre nos valores originais passados por paramêtro.
*/

// Exemplo:

function titularParaMaisculasValor(array $conta)
{
    $conta['titular'] = strtoupper($conta['titular']);
}

function titularParaMaisculasReferencia(array &$conta)
{
    $conta['titular'] = strtoupper($conta['titular']);
}

$contasCorrentes = [
    '123.456.789-10' => [
        'titular' => 'Maria',
        'saldo' => 10000
    ],
    '123.456.689-11' => [
        'titular' => 'Alberto',
        'saldo' => 300
    ],
    '123.256.789-12' => [
        'titular' => 'Vinicius',
        'saldo' => 100
    ]
];

//Modifica o valor de 'título' da cópia da conta de Maria
titularParaMaisculasValor($contasCorrentes['123.456.789-10']);

//Modifica o valor original na conta de Alberto
titularParaMaisculasReferencia($contasCorrentes['123.456.689-11']); 

// Loop para exibir mudanças
foreach ($contasCorrentes as $cpf => $conta){ // Atribuindo o nome do índice a váriavel $cpf
    echo $cpf . PHP_EOL; // Acessando o índice
    echo $conta['titular'] . PHP_EOL; // Acessando a o índice titular
}
