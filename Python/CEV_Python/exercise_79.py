valores = []

while True:
    valor = int(input('Digite um valor: '))
    if valor not in valores:
        valores.append(valor)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor já foi adicionado anteriormente!')
    continuar = input('\nDeseja continuar ? [S/N] ').upper().strip()
    while continuar[0] not in 'SsNn':
        continuar = input('Tente Novamente! Deseja continuar ? [S/N] ').upper().strip()
    if continuar[0] in 'Nn':
        break
print('=-' * 30)
valores.sort()
print(f'Os valores digitados foram: {valores}')
