peso = float(input('Digite seu peso (Kg): '))
altura = float(input('Digite sua altura (m): '))
imc = peso / (altura ** 2)
print(f'\nSeu IMC é de: {imc:.1f}.')

if imc < 18.5:
    print('Você está ABAIXO do peso!')
elif imc < 25:
    print('Você está no peso IDEAL!')
elif imc < 30:
    print('Você está em SOBREPESO!')
elif imc < 40:
    print('Você está em OBESIDADE!')
else:
    print('Você está em OBESIDADE MÓRBIDA!')
