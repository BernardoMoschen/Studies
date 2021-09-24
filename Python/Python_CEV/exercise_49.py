t = int(input('Digite um número para ver sua tabuada :'))
print('-' * 12)
print(f'Tabuada de {t}')
print('-' * 12)
for i in range(0, 11):
    print(f'{t} x {i:2} = {t * i}')
print('-' * 12)
