print('Programa que soma os números pares de 6 números inteiros.')
soma, cont = 0, 0
for i in range(0, 6):
    n = int(input(f'Digite o {1}º número inteiro: '))
    if n % 2 == 0:
        cont += 1
        soma += n
print(f'Foram somados {cont} número(s) pares e sua soma é: {soma}.')
