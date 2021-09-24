"""
--->Ranges<---

--> Precisamos conhecer o loop for para trabalhar com ranges.
--> Precisamos conhecer o range para trabalhar melhor com o loop for.

Ranges são utilizados para gerar sequências numérica, não de forma aleatórioa.
mas sim de maneira especifica.

--> Formas gerais de utilizar o range:

-> Forma 1:
range(valor_final)
# OBS: valor_final não inclusive, início padrão 0, e passo de 1 em 1.

--> Forma 2:
range(valor_inicial, valor_final)
# OBS: valor_final não inclusive, início especificado pelo usuário, e passo de 1 em 1.

--> Forma 3:
range(valor_inicial, valor_final, passo)
# OBS: valor_final não inclusive, início especificado pelo usuário, e passo especificado pelo usuário)

--> Forma 4 (Inversa):
range(valor_inicial, valor_final, passo)
# OBS: valor_final não inclusive, início especificado pelo usuário, e passo especificado pelo usuário)
"""

# Exemplo de Forma 1:
print('Exemplo da forma 1:')
for num in range(11):
    print(num)

# Exemplo de Forma 2:
print('\nExemplo da forma 2:')
for num in range(4, 11):
    print(num)

# Exemplo de Forma 3:
print('\n Exemplo de forma 3:')
for num in range(1, 10, 2):
    print(num)

# Exemplo de Forma 4 (Inversa):
print('\n Exemplo de forma 4:')
for num in range(10, -1, -1):
    print(num)