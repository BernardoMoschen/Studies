valores = []
maior = 0
menor = 0
for i in range(0, 5):
    valores.append(int(input(f'Digite o {i + 1}º valor: ')))
    if i == 1:
        maior = menor = valores[i]
    if valores[i] > maior:
        maior = valores[i]
    if valores[i] < menor:
        menor = valores[i]
print('=-' * 30)
print(f'Você digitou os valores: {valores}')
print(f'O maior valor digitado foi {maior} e sua(s) posição(ões) é: ', end='')
for c, v in enumerate(valores):
    if v == maior:
        print(f'{c}...')
print(f'O menor valor digitado foi {menor} e sua posição é: ', end='')
for c, v in enumerate(valores):
    if v == menor:
        print(f'{c}...')
