"""
---> Tipo Booleano <---

Origem na Álgebra Booleana, criada por George Boole

2 constantes, sendo elas: Verdadeiro ou Falso

True -> Verdadeiro
False -> Falso

OBS: Sempre com a inicial minúscula

Errado: true, false

Certo: True, Falso
"""

ativo = False
print('\nTipo Booleano:')
print(ativo)

"""
--> Operações básicas <--
"""

# Negação (not):
"""
Fazendo a negação, se o valor booleano for verdadeiro o resultado será falso,
se for falso o resultado será verdadeiro, ou seja, sempre o contrário
"""
print('\nNegação:')
print(not ativo)

# Ou (or):
"""
É uma operação binária, ou seja, depende de dois valores.
Ou um ou outro deve ser verdadeiro.

Exemplos:
- True or True -> True
- True or False -> True
- False or True -> True
- False or False -> False
"""
logado = False
# Como ambos são falsos, o resultado será falso.
print('\nOR:')
print(ativo or logado)

# E (and):
""" 
Também é uma operação binária, dependendo de dois valores.
Neste caso, ambos os valores devem ser verdadeiros.

Exemplos:
True and True -> True
True and False -> False
False and True -> False
False and False -> False
"""
print('\nAnd:')
num1, num2 = 5, 7
print(num1 < num2 and num1 > 3)
print(num1 > num2 and num1 <=5 )


