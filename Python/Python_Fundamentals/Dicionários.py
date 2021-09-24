"""
Dicionários são estruturas compostas/tipo de coleção.

 -> São DELIMITADOS por CHAVES " { } "
 -> São MUTÁVEIS
 -> Dicionários armazenam VALORES(values) referenciados por CHAVES(keys).
 -> A UNIÃO de VALOR e KEY resulta no ITEM, ou seja, um dicionário pode ocnter 1 ou + ITENS
"""

# Exemplo de criação de dicionário:
pessoa = {'nome': 'Bernardo', 'sexo': 'M', 'idade': 20}  # Cada valor é referenciado por uma chave
# ^Dicionário,^key,  ^valor,    ^key,  ^valor, ^key, ^valor
print(f"O {pessoa['nome']} tem {pessoa['idade']} anos", end='')  # Print dos valores de 'pessoa'
print(f"e é do sexo {pessoa['sexo']}.")

# Podemos usar o méotodo .keys() para se referir somente as KEYS do dicionário:
print(pessoa.keys())

# Assim como o método .values() refere-se somente aos VALORES do dicionário:
print(pessoa.keys())

# Ou então, podemos nos referenciar ao conjunto de ITENS do dicionário:
print(pessoa.items())

# Podemos usar ESTRUTURAS DE REPITAÇÃO para INTERAGIR com dicionários:

for key in pessoa.keys():  # Para cada KEY em dicionário.Kkeys(), ou seja, para cada laço possível em .keys():
    print(f'Chave/Key: {key}.')

for value in pessoa.values():  # Para cada VALUE em dicionário.values(), ou seja, para cada laço possível em .values():
    print(f'Valor/Value: {value}.')

for k, v in pessoa.items():  # Para cada KEY E VALOR em .items(), ou seja, para cada laço possível em .items():
    print(f'Chave/Key:{k}, Valor/Value: {v} .')

# Podemos apagar um ITEM com o comando del:
del pessoa['sexo']
print(f'{pessoa.items()}')

# Adicionar um ITEM com a sintaxe:
pessoa['peso'] = 60
print(pessoa.items())

# Modificar um ITEM com a sintaxe:
pessoa['idade'] = 21
print(pessoa.items())

# Podemos ADERIR ESTRUTURAS COMPOSTAS EM OUTRAS ESTRUTRAS COMPOSTAS:
brasil = []  # Criação de uma lista chamada 'brasil'
estado1 = {'UF': 'Rio Grande do Sul', 'sigla': 'RS'}  # Criação de dicionários chamados 'estado1/2', contendo as
estado2 = {'UF': 'São Paulo', 'sigla': 'SP'}    # chaves UF e Sigla e os valores Rio grande do Sul,RS, São Paulo e SP.
brasil.append(estado1)  # Adicionando(append) 'estado1' a lista 'brasil'
brasil.append(estado2)  # Adicionando(append) 'estado2' a lista 'brasil'
print(estado1, '\n', estado2)  # Exibindo os dicionários
print(brasil)  # Exibindo a lista brasil
print(brasil[1])  # Exibindo o 2º valor da lista brasil = o DICIONÁRIO 'estado2'
print(brasil[0]['UF'])  # Exibindo  a KEY 'UF' do 1º valor da lista 'brasil'
