nome = str(input('Digite seu nome completo: ').strip()).title()
n = nome.split()

print('É um prazer lhe conhecer !')
print(f'Seu primeiro nome é: {n[0]}.')
print(f'Seu último nome é {n[len(n) - 1]}.')
