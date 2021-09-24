print('*' * 27)
print('     Termos de uma PA     ')
print('*' * 27)
termo1 = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = termo1 + (10 - 1) * razao
soma = 0
for i in range(termo1, decimo + razao, razao):
    print(f'{i}', end=' ➜ ')
    soma += i
print('FIM')
print(f'A soma dos 10 primeiros termos é: {soma}')
