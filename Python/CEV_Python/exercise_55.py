maior = 0
menor = 0
for i in range(1, 6):
    peso = float(input(f'Digite o peso da {i}º pessoa: '))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'\nO \033[33mMENOR PESO \033[mfoi \033[33m{menor} \033[m'
      f'e o \033[31mMAIOR PESO \033[mfoi \033[31m{maior} \033[m.')
