a = int(input('Insira o primeiro valor: '))
b = int(input('Insira o segundo valor: '))
c = int(input('Insira o terceiro valor: '))
menor = a
maior = a
if b < a and b < c:
    menor = b
elif c < a and c < b:
    menor = c

if b > a and b > c:
    maior = b
elif c > a and c > b:
    maior = c

print(f'O menor valor é {menor} e o maior valor é {maior}.')
