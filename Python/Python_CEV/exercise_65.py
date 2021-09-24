soma = maior = menor = c = 0
continuar = 'S'
while continuar in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    c += 1
    if c == 1:
        menor = maior = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    continuar = input('Quer continuar? (S/N) ').upper().strip()
    while continuar not in 'SsNn':
        continuar = input('Opção inválida!\nQuer continuar? (S/N) ').upper().strip()
media = soma / c
print('=' * 35)
print(f'Você digitou {c} números, o maior foi {maior} e o menor {menor}.')
print(f'A média foi de {media:.2f}.')
