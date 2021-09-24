from random import randint
from time import sleep
from sys import exit
itens = ['Pedra', 'Papel', 'Tesoura']
computador = randint(0, 2)
print('--LETS PLAY!--')
print('Suas opções:')
print('[ 0 ] PEDRA\n[ 1 ] PAPEL\n[ 2 ] TESOURA')
jogador = int(input('Qual sua opção de jogada? '))
if jogador != 0 and jogador != 1 and jogador != 2:
    print('Opção inválida!')
    exit()
print('-=' * 7)
print('JO')
sleep(0.5)
print('    KEN')
sleep(0.5)
print('       PO')
sleep(1)
print('-=' * 7)

if computador == 0:  # Computador jogou PEDRA
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('JOGADOR VENCEU!')
    elif jogador == 2:
        print('COMPUTADOR VENCEU!')
    else:
        print('Jogada inválida!')
elif computador == 1:  # Computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCEU!!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('JOGADOR VENCEU!')
elif computador == 2:  # Computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCEU!!')
    elif jogador == 1:
        print('COMPUTADOR VENCEU!')
    elif jogador == 2:
        print('EMPATE!')
