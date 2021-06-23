grupo = []
mulheres = []
idades = media = 0
while True:
    pessoa = {'Nome': input('Nome: '),
              'Sexo': input('Sexo [M/F]: ').upper().strip()}
    while pessoa['Sexo'] not in 'MmFf':
        pessoa['Sexo'] = input('Erro! Selecione M ou F: ')
    if pessoa['Sexo'] == 'F':
        mulheres.append(pessoa['Nome'])
    pessoa['Idade'] = int(input('Idade: '))
    idades += pessoa['Idade']
    grupo.append(pessoa)
    print(pessoa.items())
    continuar = input('Deseja continuar [S/N]? ').upper().strip()
    while continuar not in 'SsNn':
        continuar = input('Erro! Responda apenas S ou N.\nDeseja continuar [S/N]? ').upper().strip()
    if continuar in 'Nn':
        break
media = idades / len(grupo)
print('=-' * 30)
print(f'A) Ao todo temos {len(grupo)} pessoas cadastradas.')
print(f'B) A média de idade é de: {media:.2f}')
if len(mulheres) >= 0:
    print('C) As mulheres cadastradas foram: ', end='')
    for p in range(0, len(mulheres)):
        print(f'{mulheres[p]}', end=' ')
