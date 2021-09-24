numeros = (int(input('Digite um número: ')),
           int(input('Digite outro número: ')),
           int(input('Digite mais um número: ')),
           int(input('Digite o último número: ')))
print(f'\nVocê digitou os valores: {numeros} .')
print(f'O número 9 apareceu {numeros.count(9)} vezes.')
if 3 in numeros:
    print(f'O 1º valor 3 foi digitado na {numeros.index(3)}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
print(f'Os valores pares digitados foram: ', end='')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')
