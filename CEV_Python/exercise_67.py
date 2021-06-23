tab = 0
while tab >= 0:
    print('-' * 11)
    tab = int(input('Tabuada de qual número ? \n(Negativo para encerrar)\nNúmero: '))
    if tab < 0:
        break
    c = 1
    while c <= 10:
        print(f'{tab} x {c} = {tab * c}')
        c += 1
