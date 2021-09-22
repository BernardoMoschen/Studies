par = int(input('Digite o número a ser analisado: '))
print(f'Analisando os números pares no intervalo de 0 a {par}...')
print('Os números pares são: ', end='')
for par in range(0, par + 1, 2):
    print(par, ' ', end='')
