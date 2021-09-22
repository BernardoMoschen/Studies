contagem = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
            'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    i = int(input('Digite um número entre 0 e 20: '))
    if 0 < i > 20:
        i = int(input('Tente novamente.\nDigite um número entre 0 e 20: '))
    print(f'\nVocê digitou o número {contagem[i]}.')
    continuar = str(input('Deseja continuar ? [S/N] ')).strip().upper()
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar ? [S/N] ')).strip().upper()
    if 'N' in continuar[0]:
        break
