print('=' * 5 + 'LOJAS MOSCHEN' + '=' * 5)
compras = float(input('Digite o preço total das compras: R$'))
print('\n--Formas de Pagamento--')
print('[ 1 ] à vista no dinheiro/cheque')
print('[ 2 ] à vista no cartão')
print('[ 3 ] 2x sem juros no cartão')
print('[ 4 ] 3x ou mais no cartão, com 20% de juros')
escolha = int(input('Qual a opção de pagamento? '))

if escolha == 1:
    total = compras - (compras * 10 / 100)
elif escolha == 2:
    total = compras - (compras * 5 / 100)
elif escolha == 3:
    total = compras
    print(f'\nSua compra será parcelada em 2x de R${total / 2:.2f}.', end='')
elif escolha == 4:
    total = compras + (compras * 20 / 100)
    parcelas = int(input('Quantas parcelas? '))
    print(f'\nSua compra será parcelada em {parcelas}x de R${total / parcelas :.2f}.', end='')
else:
    total = compras
    print('\nVocê digitou uma opção inválida.\nTente novamente!', end='')
print(f'\nO total custará R${total:.2f}.')
