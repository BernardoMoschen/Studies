"""
 --->Estruturas condicionais if, else, elif<----

 Estrutura if (se) : se condicional verdadeira, faça.

"""

idade = int(input('Digite sua idade:'))
if idade < 18:
    print('Menor de idade.')
elif 0 < idade > 100:
    print('O valor digitado é errôneo.')
else:
    print('Maior de idade')
