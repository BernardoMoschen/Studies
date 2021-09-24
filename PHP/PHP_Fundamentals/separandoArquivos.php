<?php

/* A divisão e 'importação' de arquivos no php é feita por:

=> include 'nomeDoArquivo.extensão'
    Inclui o arquivo e executa/traz todo o código presente nele.

=> require 'nomeDoArquivo.extensão'
    Funciona do mesmo modo que o 'include', porém, torna a sua importação obrigatória,
     ou seja, impede que o código que está realizando a importação porssiga casa haja
      a ausência da importação
      
=> require_once 'nomeDoArquivo.extensão'
    Funciona do mesmo modo que o 'require', porém, só realiza a importaçao 1 vez.
     Caso a importação ainda não tenha sido efetuada.
*/