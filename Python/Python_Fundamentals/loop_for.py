"""
 ---> Loop for <---

--->Loop: É uma estrutura de repetição.
Loops são utilizados para iterar sobre sequências ou sobre valores iteráveis.
-->Exemplos de iteráveis:
- String
    nome = "Bernardo's Studies"
- Lista
    lista = [1, 2, 5, 7, 12]
- Range
    numeros = range(1, 10)


--->For: Integra uma dessas estruturas.

-->Esqueleto da estrutura for:
for item in interável:
    //execução do loop       # Obs: para a indentação, utiliza-se 4 espaços.

-->Enumarate():
Permite o desenvolvimento de loops for quando há a necessidade de uma contagem e
do valor de um iterável.Criando assim uma tupla(tuple) com um contado e um valor,
sem a necessidade de incrementar o contador.

-->Exemplo:
enumarate(nome):
((0, 'B'), (1, 'e'), (2, 'r'), (3,'n'), (4, 'a'), (5, 'r'), (6, 'd'), (7,'o') ...)

for indice, letra in enumarate(nome):
    print(nome[indice])

for indice, letra in enumarate(nome):
    print(letra)

for _, letra in enumarate(nome):    # Quando não precisamos de um valor, pode-se
    print(letra)                    descartá-lo usando unerline(_).
"""

# Definindo as variáveis para teste
nome = "Bernardo's Studies"
lista = [1, 2, 5, 7, 12]
numeros = range(1, 10)  # Transformaremos em uma lista

# Exemplo de for 1 - Iterando sobre uma string:
print('Iterando sobre uma String com for:')
for letra in nome:
    print(letra)

# Exemplo de for 1.1 - Iterando sobre uma string:
print('Iterando sobre uma String com for:')
for letra in nome:
    print(letra, end='')


# Exemplo de for 2 - Iterando sobre uma lista:
print('\nIterando sobre uma lista com for:')
for numero in lista:
    print(numero)

# Exemplo de for 3 - Iterando sobre um range:
print('\nIterando sobre um range com for:')
# for numero in numeros:
# print(numero)

for numero in range(1, 10):
    print(numero)

# Exemplo de for 3.1 - Iterando sobre um range:
print('\nIterando sobre um range com for:')
qtd = int(input('Quantas vezes este loop deve acontecer?'))
soma = 0
for n in range(1, qtd+1):
    num = int(input(f'Informe o valor {n}/{qtd}:'))
    soma = soma + num
print(f'O resultado da soma é: {soma}')

#Exemplo de for 3.2 - Iterando sobre um range:
print('\nIterando sobre um range com for:')
for _ in range(3):
    for num in range(1, 11):
        print("\U0001F332" * num)


"""
Trabalhando com range:
range(valor_inicial, valor_final)

Obs: O valor final não é inclusive, pois a contagem inicia em 0.
Ou seja, em um range(1, 10):
1
2
3
4
5
6
7
8
9
10 - Não inclusive.
"""
