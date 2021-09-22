larg = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
area = larg * alt
tinta = area / 2
print(f'Sua parede possuí a dimensão de {larg} X {alt}, sendo assim, sua área é de {area} .')
print(f'Para pintá-la, você precisará de {tinta:.2f}l de tinta.')
