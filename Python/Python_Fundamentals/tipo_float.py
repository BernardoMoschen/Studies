"""
---> Tipo Float <---

Tipo real, decimal

Casas decimais

OBS: o separador de casas decimais na programação por padrão é : " . "
"""

# Errado do ponto de vista do Float, pois gera uma Tupla
valor = 1, 44
print(valor)
print(type(valor))


# Certo do ponto de vista Float
valor =  1.44
print(valor)
print(type(valor))

# Mas também é possível realizar dupla atribuição em apenas 1 só linha
valor1, valor2 = 1, 44
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

# É possível a conversão de um Float para um Inteiro
"""
OBS: Na conversão dos valores de float para inteiro, há perda de precisão.
"""
res = int(valor)
print(res)
print(type(res))

# Assim como também podemos converter um Inteiro para Float
var = float(res)
print(var)
print(type(var))

# Podemos trabalhar com n°s complexos
variavel =5j