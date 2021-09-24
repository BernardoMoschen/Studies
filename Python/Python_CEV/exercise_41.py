from datetime import date
anoNascimento = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - anoNascimento

print(f'O atleta tem {idade} anos.')
if idade < 9:
    print('Sua classificação é: MIRIM.')
elif idade < 14:
    print('Sua classificação é: INFANTIL.')
elif idade < 19:
    print('Sua classificação é: JUNIOR.')
elif idade < 25:
    print('Sua clasificação é: SÊNIOR.')
else:
    print('Sua classificação é: MASTER.')
