import math
ang = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(ang))
cosseno = math.cos(math.radians(ang))
tangente = math.tan(math.radians(ang))

print(f'O ângulo {ang:.2f} possui o Seno no valor de {seno:.2f} .')
print(f'O ângulo {ang:.2f} possi o Cosseno no valor de {cosseno:.2f} .')
print(f'O ângulo {ang:.2f} possui a Tangente no valor de {tangente:.2f} .')
