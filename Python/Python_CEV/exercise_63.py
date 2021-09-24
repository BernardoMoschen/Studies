print('\033[32m>' * 7, 'Sequência de Fibonacci', '<' * 7)
termos = int(input('Quantos termos você deseja mostrar? '))
tot1 = 0
tot2 = 1
print('\033[m=' * (termos * 7))
print(f'\033[33m{tot1}  ➜  {tot2}', end='')
i = 3
while i <= termos:
    tot3 = tot1 + tot2
    print(f' ➜ {tot3}', end='')
    tot1 = tot2
    tot2 = tot3
    i += 1
print(' ➜ Fim')
print('\033[m=' * (termos * 7))
