from random import randint

print('Gerando um número aleatório para você tentar adivinhar...\nVocê possui 5 tentativas!')
num = int(randint(0, 5))
tentativas = 5

while tentativas > 0:
    chute = int(input('Digite o número de 0 a 5 que você deseja chutar: '))
    if chute == num:
        print('\nParabéns! Você acertou!')
        break
    else:
        print('\nVocê errou. Tente novamente !')
        tentativas -= 1
        print(f'Restam {tentativas} tentativas!')

if tentativas == 0:
    print('\nVocê esgotou suas tentativas !')
