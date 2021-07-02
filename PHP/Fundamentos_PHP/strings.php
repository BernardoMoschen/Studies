<?php

/* Realizamos a declaração de strigns em PHP utilizando aspas simples ou duplas.

=> Diferenças entre tipos de aspas:
    - Aspas simples ('') são tidas diretamente como textos.
    - Aspas duplas ("") são realmente interpretas, desta forma, se houver variáveis ou caracteres entre o texto, o interpretador do PHP os levará em consideração.

=> Concatenação:
    Feita por '.' entre as variáveis.
ex: 'João tem' . $idade . ' anos.;

=> Quebras de linha:
    \n - new line
    \t - new tab
    \r - new line (para windows)
        
        OBS: Álias, para realizar uma quebra de linha em SO Windows, deve-se usar '\r\n'.
        Para contornar isto, o PHP disponibiliza o 'PHP_EOL', ou, PHP_EndOfLine
*/

// Alguns exemplos:
$idade = 16;
echo "Olá mundo!" . PHP_EOL;
echo "Eu tenho \"$idade\" anos";

echo PHP_EOL . PHP_EOL;

echo "Você só pode entrar, se tiver mais de 18 anos\n";

echo "Você tem $idade anos. Pode entrar";