<?php

$peso = 63;
$altura = 1.69;
$imc = $peso / $altura ** 2;

echo "Seu IMC é de $imc." . PHP_EOL . "Você está com o IMC ";

if ($imc < 18.5) {
    echo "abaixo";
} else if ($imc < 25) {
    echo "dentro";
} else {
    echo "acima";
}

echo " do recomendado";
