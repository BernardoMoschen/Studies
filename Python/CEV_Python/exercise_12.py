prod = float(input('Digite o preço do produto: R$'))
desct = float(input('Digite o desconto a ser aplicado sobre o produto: %'))
preço = (prod) - prod * desct / 100
print(f'O preço final do produto com o desconto já aplicado é de R${preço:.2f} .')

#print(f'O preço final do produto com o desconto já aplicado é de R${(prod) - prod * desct / 100:.2f} .')
