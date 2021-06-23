salario = float(input('Digite o salário do funcionário: R$'))
aumento = float(input('Digite a porcentagem de aumento a ser aplicada: %'))
salarioF = (salario) + salario * aumento / 100
print(f'O salário final do funcionário já aplicado o aumento é de R${salarioF:.2f} .')

#print(f'O salário final do funcionário já aplicado o aumento é de R${(salario) + salario * aumento / 100 } .')
