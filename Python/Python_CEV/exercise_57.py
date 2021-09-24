sexo = str(input('Digite o sexo da pessoa [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    print('\nDados inválidos, por favor, tente novamente.')
    sexo = str(input('Digite o sexo da pessoa [M/F]: ')).strip().upper()[0]
if sexo == "M":
    print(f'Sexo masculino registrado no sistema com sucesso!')
else:
    print('Sexo feminino registrado no sistema com sucesso!')
