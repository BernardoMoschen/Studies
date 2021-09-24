from datetime import date
maiores = 0
menores = 0
for pess in range(1, 8):
    nascimento = int(input(f'Em que ano a {pess}ª pessoa nasceu? '))
    idade = date.today().year - nascimento
    if idade >= 18:
        maiores += 1
    else:
        menores += 1
print(f'Ao total foram analisadas \033[31m{menores} pessoas menores \033[me \033[033m{maiores} maiores de idade.')
