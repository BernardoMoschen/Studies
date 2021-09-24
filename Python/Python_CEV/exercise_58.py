from random import randint
num = randint(0, 10)
tentativas = 5
chute = 0
print('=' * 7, 'Vamos jogar!', '=' * 7)
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? \U0001F928')
print('Vou lhe dar 5 tentativas!\n')

while tentativas > 0:
    chute = int(input('Digite o seu palpite: '))
    if chute == num:
        print('\nParabéns! Você acertou!')
        break
    elif chute != num:
        if chute > num:
            print('\nO número é MENOR, tente novamente !')
            tentativas -= 1
            print(f'Restam {tentativas} tentativas!')
        elif chute < num:
            print('\nO número é MAIOR, tente novamente!')
            tentativas -= 1
            print(f'Restam {tentativas} tentativas!')
print(f'O número secreto era {num} e você só precisou de {5 - tentativas} tentativas!')
