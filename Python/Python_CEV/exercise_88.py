from random import randint
print('-' * 30)
print(" " * 5, "JOGO DA MEGA SENA")
print('-' * 30)
jogo = []
jogos = int(input('Quantos jogos você deseja que eu sorteie? '))
print('=-' * 3, f'SORTEANDO {jogos} JOGOS', '=-' * 3)
for i in range(1, jogos+1):
    print(f'Jogo {i}: ', end='')
    for n in range(0, 6):
        jogo.append(randint(0, 60))
    print(jogo)
    jogo.clear()
print('=-' * 5, f'BOA SORTE!', '=-' * 5)
