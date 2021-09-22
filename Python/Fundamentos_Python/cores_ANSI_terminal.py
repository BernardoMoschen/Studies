"""
---Padrão de sequências de escape ANSI para cores no terminal (sem módulo, como o 'Colorize':

 -->CÓDIGO PADRÃO: \033[tipoEstilo;corTexto;corFundo;m

 -->ESTILO DE FONTE:
   -> O = Padrão
   -> 1 = Negrito.
   -> 4 = Sublinhado.
   -> 7 = Negativo.

 -->COR DO TEXTO:
   -> 30 = Branco.
   -> 31 = Vermelho.
   -> 32 = Verde.
   -> 33 = Amarelo.
   -> 34 = Azul.
   -> 35 = Rosa.
   -> 36 = Ciano.
   -> 37 = Cinza.

   -->COR DE FUNDO:
   -> 40 = Branco.
   -> 41 = Vermelho.
   -> 42 = Verde.
   -> 43 = Amarelo.
   -> 44 = Azul.
   -> 45 = Rosa.
   -> 46 = Ciano.
   -> 47 = Cinza.
"""

# Exemplos:

# Letra em Negrito, texto em Laranja e fundo em Amarelo:
print('\033[1;31;43mOlá, Mundo!')

# letra Sublinha, texto Branco, fundo Rosa, VOLTANDO A COLORAÇÃO NORMAL:
print('\033[4;30;45mOlá, Mundo!\033[m')

# Letra Branca, texto Negativo, fundo Preto, VOLTANDO A COLORAÇÃO NORMAL:
print('\033[7;30mOlá, Mundo!\033[mCor normal !')
