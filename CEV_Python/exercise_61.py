print('>' * 7, 'Gerador de PA', '<' * 7)
termo1 = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
primeiro = termo1
i = 1
while i <= 10:
    print(f'{primeiro}', end=' ➜ ')
    primeiro += razao
    i += 1
print('Fim.')
