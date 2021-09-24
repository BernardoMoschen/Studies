print('Para realizar a aprovação do seu parcelamento, preciso que: ')
vlrCasa = float(input('Digite o valor do imóvel: R$'))
salr = float(input('Digite o valor do seu salário: R$'))
qtdPrestc = float(input('Digite a quantidade de anos desejada: '))

vlrPrestc = vlrCasa / (qtdPrestc * 12)
maxSalr = salr * 30 / 100
print(f'Para um empréstimo de {qtdPrestc} anos, o valor da prestação será de R${vlrPrestc:.2f}.')

print('Analisando...')
if vlrPrestc < maxSalr:
    print('\nEmpréstimo Aprovado!')
elif salr > vlrCasa:
    print('\nWOW.\nVocê pode comprar a casa à vista!')
else:
    print('\nEmpréstimo Negado!')
    print('Você não possui renda suficiente e a prestação equivaleria a mais de 30% do seu salário.')
