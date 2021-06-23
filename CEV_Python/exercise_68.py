from random import randint
from time import sleep

print('*' * 30, '\n', ' ' * 4, 'JOGO DO PAR OU ÍMPAR', '\n', '*' * 30)
while True:
    wins = 0
    print('Você desejar ser PAR ou ÍMPAR ?')
    escolha = int(input('[1] ÍMPAR\n[2] PAR\nOpção: '))
    while escolha != 1 and escolha != 2:
        print('~' * 32)
        print('Opção inválida! Tente novamente!')
        escolha = int(input('[1] ÍMPAR\n[2] PAR\nOpção: '))
    if escolha == 1:
        print('Você será ÍMPAR e o computador será PAR.')
    else:
        print('Você será PAR e o computador será ÍMPAR.')
    jogada = int(input('\nQual será sua jogada? '))
    print('=' * 15, '\nPAR')
    sleep(1)
    print(' ' * 5, 'OU')
    sleep(1)
    print(' ' * 10, 'ÍMPAR\n', '=' * 15)
    computador = randint(1, 10)
    resultado = (jogada + computador) % 2
    if resultado == 0 and escolha == 2:
        print('Você Venceu!')
        wins += 1
    elif resultado != 1 and escolha == 1:
        print('Você venceu!')
        wins += 1
    else:
        print('Você perdeu!')
        break
if wins > 0:
    print(f'Mas conseguiu vencer {wins} vezes consecutivas !\nParabéns!')
else:
    print('E não venceu 1 vez sequer!')
