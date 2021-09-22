soma, cont = 0, 0
impar = int(input('Digite o número a ser analisado: '))
print(f'Analisando os números ímpares no intervalo de 0 a {impar}...')
for impar in range(1, impar + 1, 2):
    if impar % 3 == 0:
        cont += 1
        soma += impar
print(f'A soma de todos os números ímpares múltiplos de 3 ({cont}) no intervalo de 0 a {impar + 1} é: {soma}.')
