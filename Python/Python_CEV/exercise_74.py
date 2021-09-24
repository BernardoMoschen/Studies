from random import randint
aleat = (randint(0, 5), randint(0, 5), randint(0, 5), randint(0, 5), randint(0, 5))

print('Os valores sorteados foram: ', end='')
for i in aleat:
    print(f'{i} ', end='')
print(f'\nO maior sorteado sorteado foi: {max(aleat)}')
print(f'O menor valor sorteado foi: {min(aleat)}')
