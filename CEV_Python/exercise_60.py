num = int(input('Digite um número para calcular seu fatorial: '))
i = num
fatorial = 1
while i > 0:
    print(f'{i}', end='')
    print(' x ' if i > 1 else ' = ', end='')
    fatorial *= i
    i -= 1
print(f'{fatorial}.')
