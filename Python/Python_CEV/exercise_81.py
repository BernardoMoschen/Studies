numeros = []

while True:
    numeros.append(int(input('Digite um valor: ')))
    continuar = input('Quer continuar? [S/N] ').upper().strip()
    while continuar[0] not in 'SsNn':
        continuar = input('Tente Novamente.\nQuer continuar? [S/N] ').upper().strip()
    if continuar in 'Nn':
        break

print(f'Foram digitados {len(numeros)} valores.')
numeros.sort()
print(f'Os valores digitados em ordem CRESCENTE foram:')
numeros.sort(reverse=True)
print(f'Os valores digitados em ordem DECRESCENTE foram:')
if 5 in numeros:
    print(f'O valor 5 foi digitado e está na posição {numeros.index(5)}')
else:
    print('O valor 5 não foi encontrado.')
