velocidade = float(input('Insira a velocidade atual do veículo (Km/h): '))

if velocidade > 80.0:
    print('\nO veículo em questão excedeu o limite de 80Km/h e foi multado!')
    multa = (velocidade - 80.0) * 7.0
    print(f'O valor da multa a pagar é de R${multa:.2f}')
else:
    print('O veículo não foi multado.')
    print('Obrigado por dirigir com segurança !')
