from math import hypot
# import math

oposto = float(input('Digite o comprimento do cateto oposto: '))
adjacente = float(input('Digite o comprimento do cateto adjacente: '))
hi = (oposto ** 2 + adjacente ** 2) / (1/2)
hi2 = hypot(oposto, adjacente)
print(f'A hipotenusa mede {hi:.2f} .')
print(f'A hipotenusa mede {hi2} .')
