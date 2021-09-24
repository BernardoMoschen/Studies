bras = ('Flamengo', 'Internacional', 'Atéltico-MG', 'São Paulo', 'Fluminense', 'Grêmio', 'Palmeiras',
        'Atlético-PR', 'Bragantino', 'Ceará', 'Corinthians', 'Atlético-GO', 'Bahia', 'Sport', 'Fortaleza',
        'Vasco', 'Goiás', 'Chapecoense', 'Botafogo')
print('---5 PRIMEIROS---')
for cont in range(0, 5):
    print(bras[cont])

print('\n---4 ÚLTIMOS---')
for cont in range(15, 19):
    print(bras[cont])

print('\n---EM ORDEM ALFABÉTICA---')
for cont in range(0, len(bras)):
    print(sorted(bras)[cont])

print(f"\nA Chapecoense está na posição: {bras.index('Chapecoense')}")
