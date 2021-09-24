print('=' * 30)
print('{:^30}'.format('Banco BeeMo'))
print('=' * 30)
valor = int(input('Que valor você quer sacar? '))
total = valor
cedulas = 50
totCed = 0
while True:
    if total >= cedulas:
        total -= cedulas
        totCed += 1
    else:
        if totCed > 0:
            print(f'Total de {totCed} cédula(s) de R${cedulas}.')
        if cedulas == 50:
            cedulas = 20
        elif cedulas == 20:
            cedulas = 10
        elif cedulas == 10:
            cedulas = 1
        totCed = 0
        if total == 0:
            break
print('*' * 30)
print('Volte Sempre!')
