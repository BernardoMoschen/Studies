real = float(input('Digite a quantidade de dinheiro a ser convertida: R$'))
dolar = float(input('Digite a cotação do dólar: US$'))
print(f'Com R${real:.2f} você poderá comprar o equivalente à US${real / dolar:.2f} .')
