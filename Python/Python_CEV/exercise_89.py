ficha = []
while True:
    nome = input('Digite o nome do aluno: ')
    nota1 = float(input('Digite a 1º nota: '))
    nota2 = float(input('Digite a 2º nota: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    continuar = input('Quer continuar? [S/N]')
    print('')
    while continuar not in 'SsNn':
        continuar = input('\nTente novamente.\nQuer continuar? [S/N]')
    if continuar in 'Nn':
        break
print('-=' * 30)
print(f'{"Nº":<4}{"Nome":<10}{"Media":>8}')
print('-' * 20)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
print('-' * 20)
while True:
    mostrar = int(input('Mostar notas de qual aluno? [999 p/ interromper] :'))
    if mostrar == 999:
        print('Finalizando....')
        break
    if mostrar <= len(ficha) - 1:
        print(f'Notas de {ficha[mostrar][0]} são {ficha[mostrar][1]}')
