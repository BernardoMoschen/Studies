print('---CONVERTOR DE BASES---')
num = int(input('Digite o número inteiro a ser convertido: '))
print(' [ 1 ] converter em BINÁRIO.')
print(' [ 2 ] converter em OCTAL.')
print(' [ 3 ] converter em HEXADECIMAL.')
opcao = int(input('Com base na lista acima, digite sua opção: '))

if opcao == 1:
    print(f'\nO número {num} convertido em binário resulta em: {bin(num)[2:]}.')
elif opcao == 2:
    print(f'\nO número {num} convertido em octal resulta em: {oct(num)[2:]}.')
elif opcao == 3:
    print(f'\nO número {num} convertido em hexadecimal resulta em: {hex(num)[2:]}.')
else:
    print('\nVocê digitou uma opção inválida.\nTente novamente!')
