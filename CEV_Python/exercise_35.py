print('-=' * 20 + '\n' + ' ' * 7 + 'Analisador de Triângulos' + '\n' + '-=' * 20)

reta1 = float(input('Informe a primeira reta: '))
reta2 = float(input('Informe a segunda reta: '))
reta3 = float(input('Informe a terceira reta: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('\nAs retas informadas podem formar um triângulo!')
else:
    print('\nAs retas informadas não podem formar um triângulo.')
