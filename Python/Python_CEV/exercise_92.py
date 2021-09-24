from datetime import datetime
trabalhador = {'Nome': input('Nome: '),
               'Idade': int(input('Ano de nascimento: ')),
               'Carteira de Trabalho': int(input('Carteira de trabalho (0 se não tem): '))}
trabalhador['Idade'] = datetime.today().year - trabalhador['Idade']
if trabalhador['Carteira de Trabalho'] != 0:
    trabalhador['Ano de Contratação'] = int(input('Ano de contratação: '))
    trabalhador['Salário'] = float(input('Salário: R$'))
    trabalhador['Aposentadoria'] = trabalhador['Idade'] \
        + (trabalhador['Ano de Contratação'] + 35) - datetime.today().year
print('=-' * 30)
for k, v in trabalhador.items():
    print(f"{k} possui o valor {v}.")
