dist = float(input('\nDigite a distância da viagem: '))
print(f'Você solicitou uma viagem de {dist}Km.')
preco = dist * 0.50 if dist <= 200 else dist * 0.45
print(f'O preço final de sua passagem será de R${preco:.2f}.')

"""if dist <= 200:
    print(f'O valor não é promocional.')
    print(f'O preço total de sua passagem é de R${dist * 0.50} .')
elif dist >= 200:
    print(f'O valor é promocional!')
    print(f'O preço total de sua passagem é de R${dist * 0.45} .')
"""
