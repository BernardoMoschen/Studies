num = soma = c = 0
while num != 999:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    soma += num
    c += 1
print('=' * 57)
print(f'Foram digitados {c} números e a soma total deles é de: {soma}.')
