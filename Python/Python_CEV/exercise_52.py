num = int(input('Digite um número: '))
total = 0
for i in range(1, num + 1):
    if num % i == 0:
        print('\033[33m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print(f'{i}', end=' ')
print(f'\n\033[mO número {num} foi divisível {total} vezes.')
if total == 2:
    print('Portanto, ele é um número PRIMO!')
else:
    print('Portanto, ele NÃO é PRIMO!')
