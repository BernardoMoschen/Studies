"""
---> Tipo String <---

-->Em Python, um dado é considerado do tipo string sempre que:
- Estiver entre àspas simples -> 'uma string', '234', 'a', 'True', '42.3'
- Estiver entre àspas  duplas -> "uma string", "234, "a", "True", "42.3"
- Estiver entre àspas simples triplas -> '''uma string''', '''234''', '''a''', '''True''', '''42.3'''    """
# - Estiver entre àspas duplas triplas -> """uma string""", """234""", """a""", """True""", """42.3"""

"""
-->Quando criamos uma string, o Python a organiza neste padrão:
string exemplo: 'Maria Joaquina'
['M', 'a', 'r', 'i', 'a', ' ', 'J', 'o', 'a', 'q', 'u', 'i', 'n', 'a']
[ 0,   1,   2,   3,   4,   5,   6,   7,   8,   9,  10,   11,  12,  13]
Ou seja, uma string é um grupo de caracteres agrupados,onde cada um possui um valor referencial.



-->Podemos interagir com strings, usando comandos como: 
- print(nome.upper()) -> Transforma todas as letras da string em maiúsculas e imprime
- print(nome.lower()) -> Transforma todas as letras da string em minúsculas e imprime
- print(nome.split()) -> Transforma em uma lista de strings e imprime
- print(nome[10]) -> Imprime o caractere de n° 15 da string
- print(nome[0:6] -> Imprime apenas uma parte de uma string
- print(nome[::-1]) ->Inverte a string
"""

"""
Exemplos:
"""
# O uso mais comum é o de àspas simples:
nome = 'Estudo de Bernardo'
print('\nUsando aspas simples:')
print(nome)
print(type(nome))

# Porém, em alguns casos, há necessidade de àspas dentro da própria string.
# Neste caso, usa-se àspas duplas:
print('\nUsando aspas duplas:')
nome1 = " Pietro's Bar "
print(nome1)
print(type(nome1))

# Usando àspas triplas podemos evitar o uso de de quebra de linha via "\n":
nome2 = 'Michael \nFassbender'
print('\nUsando aspas triplas:')
print(nome2)
print(type(nome2))

nome3 = """Michael
Fassbender"""
print(nome3)
print(type(nome3))


# Usando .upper :
print('\nUsando .upper:')
print(nome.upper())
print(type(nome))


# Usando .lower :
print('\nUsando .lower:')
print(nome.lower())
print(type(nome))


# Usando .split :
print('\nUsando .split:')
print(nome.split())
print(type(nome))
#Resultado:
#['Estudo', 'de', 'Bernardo']

#Podemos exibir somente parte da string:
print('\nUExibindo somente parte de uma string:')
print(nome.split()[1])
print(type(nome))
#Resultado:
#'de'


# Acessando somente um caractere de uma string:
print('\nAcessando somente um caractere de uma string:')
print(nome[0], nome[10])
print(type(nome))
#Resultado:
#'E''B'

# Acessando somente uma parte de uma string:
print('\nAcessando somente uma parte de uma string:')
print(nome[0:6])
print(type(nome))
#Resultado:
#'Estudo'

# Invertendo a string:
print('\nInvertendo a string:')
print(nome[::-1])
print(type(nome))
#Resultado:
#'odranreB ed odutsE'


# Substituindo um caractere da string:
print('\nSubstituindo caractere(s) da string:')
print(nome.replace('o', 'i'))
#Resultado:
#'Estudi de Bernardi'