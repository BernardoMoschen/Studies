print('>' * 11, 'Adicionador de números', '<' * 11)
cont, soma = 0, 0
num = int(input('Digite um número (999 p/ encerrar): '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número (999 p/ encerrar): '))
print('=' * 46)
print(f'A soma total dos {cont} números digitados é de: {soma}.')
