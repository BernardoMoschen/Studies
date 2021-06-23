print('-' * 37)
print(' ' * 9, 'LOJA TUDO BARATÃO', ' ' * 10)
print('-' * 37)
prodtMaisBarato = ''
c = total = precoMaisBarato = prodtsCaros = 0
while True:
    nomeProd = str(input('Digite o nome do produto: ')).title()
    precoProd = float(input('Preço: R$'))
    c += 1
    total += precoProd
    if c == 1 or precoProd < precoMaisBarato:
        precoMaisBarato = precoProd
        prodtMaisBarato = nomeProd
    if precoProd > 1000:
        prodtsCaros += 1
    continuar = '1'
    print('- ' * 15)
    while continuar not in 'SN':
        continuar = str(input('Quer continuar [S/N]: ')).upper().strip()
        if 'N' != continuar != 'S':
            print('Opção Inválida! Tente novamente.')
    if continuar == 'N':
        break

print('{:-^40}'.format('Fim do Programa'))
print(f'O total da compra foi R${total:.2f}.')
print(f'Há {prodtsCaros} produto(s) custando mais de R$1000.00')
print(f'O produto mais barato foi: {prodtMaisBarato}.')
