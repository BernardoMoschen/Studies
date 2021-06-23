totalPessoas = maiorIdade = mulheresMenores = homens = 0

while True:
    print('-' * 30)
    print('      CADASTRE UMA PESSOA    ')
    print('-' * 30)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()
    if sexo == 'M':
        homens += 1
    if idade > 18:
        maiorIdade += 1
    if sexo == 'F' and idade < 20:
        mulheresMenores += 1
    print('=' * 30)
    continuar = ''
    while continuar not in 'SN':
        continuar = str(input('Quer continuar [S/N]: ')).upper().strip()
        if 'N' != continuar != 'S':
            print('Opção Inválida! Tente novamente.')
    if continuar == 'N':
        break
    totalPessoas += 1
print(f'\nO total de pessoas com mais de 18 anos é de: {maiorIdade}.')
print(f'Ao todo há {homens} homen(s) cadastrados.')
print(f'E temos também {mulheresMenores} mulhere(s) com menos de 20 anos.')
