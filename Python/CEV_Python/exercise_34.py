salario = float(input('Digite o salário do funcionário: R$'))

if salario > 1.250:
    print(f'\nO salário de R${salario} sofreu 10% de aumento.')
    salario = salario + (salario * 10 / 100)
elif salario <= 1.250:
    print(f'\nO salário de R${salario} sofreu 15% de aumento.')
    salario = salario + (salario * 15 / 100)
print(f'O salário passou a ser R${salario:.2f} .')