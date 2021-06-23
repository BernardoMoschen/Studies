print('>' * 7, 'Gerador de PA', '<' * 7)
termo1 = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
primeiro = termo1
i = 1
total = 0
numTermos = 10
while numTermos != 0:
    total += numTermos
    while i <= total:
        print(f'{primeiro}', end=' ➜ ')
        primeiro += razao
        i += 1
    print('Pausa.')
    numTermos = int(input('Quantos termos a mais você deseja? (0 = nenhum) '))
print(f'\nA progressão foi finalizada e foram mostrados {total} termos.')
