reta1 = int(input('Digite o primeiro segmento: '))
reta2 = int(input('Digite o segundo segmento: '))
reta3 = int(input('Digite o terceiro segmento: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('\nAs retas informadas podem formar um triângulo ', end='')
    if reta1 == reta2 == reta3:
        print('EQUILÁTERO!\nPois todos os seus lados são iguais.')
    elif reta1 != reta2 != reta3 != reta1:
        print('ESCALENO!\nPois todos os seus lados são diferentes.')
    else:
        print('ISÓSCELES!\nPois há dois lados iguais.')
else:
    print('\nAs retas informadas não podem formar um triângulo.')
