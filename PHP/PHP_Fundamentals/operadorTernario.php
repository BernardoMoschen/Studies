<?php

/*

=> Operador ternário:
    Os operadores ternários podem ser usados quando há a necessidade de realizarmos uma verificação lógica em apenas uma linha, 
    
    -> Estrutura:
        experessão lógica ? resultado caso true : resultado caso false
*/

// Exemplo:

$idade = 18;
$numeroDePessoas = 2;

echo "Você só pode entrar se tiver a partir de 18 anos ou ";
echo "a partir de 16 anos acompanhado." . PHP_EOL;

$mensagem = $idade < 18 ? 'você é menor de idade.' : 'você é maior de idade.';

echo "Sua idade é $idade, logo $mensagem";