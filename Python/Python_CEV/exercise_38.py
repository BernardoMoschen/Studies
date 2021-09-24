print('---Comparador de números inteiros---')

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 > n2:
    print(f'\nO primeiro valor ({n1}) é maior!')
elif n2 > n1:
    print(f'\nO segundo valor ({n2}) é maior!')
else:
    print('Não há maior.\nOs números são iguais! ')
