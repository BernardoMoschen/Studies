"""
Listas são estruturas de dados composta por itens organizados de forma linear,
onde cada elemento recebe um índice que representa sua posição na coleção,

-Listas são representadas por [ ] (colchetes)
-Listas são MUTÁVEIS
-Listas começam do índice 0
"""

# Exemplos de uso de LISTAS e seus MÉTODOS

num = [2, 9, 5, 10]  # Definição de uma lista
num[2] = 8  # Mutando a lista, substituindo o valor de um índice
num.append(7)  # MÉTODO para ADICIONAR um item AO FINAL DA LISTA = .apend(VALOR)
num.sort()  # MÉTODO para ORDENAR uma lista de forma CRESCENTE
num.sort(reverse=True)  # MÉTODO para ORDENAR REVERSAMENTE, ou seja, de forma DECRESCENTE
num.insert(2, 0)  # MÉTODO para INSERIR UM VALOR em uma posição ESPECÍFICA = .insert(POSIÇÃO, VALOR)
num.pop(2)  # MÉTODO p/ EXCLUIR um valor da lista, pelo seu ÍNDICE = .pop(ÍNDICE)
num.pop()  # MÉTODO p/ EXCLUIR o valor FINAL DA LISTA, SEM PARÂMETRO = .pop()
num.remove(9)  # MÉTODO p/ REMOVER a PRIMEIRA OCORRÊNCIA de um VALOR ESPECIFÍCO = .remove(VALOR)
print(f'Essa lista tem {len(num)} elementos.')  # Exibindo o comprimento da lista.
print(num)

a = [2, 3, 4, 7]  # Definição de uma lista
b = a  # Desta forma, AS LISTAS SÃO INTERLIGADAS, NÃO COPIADAS
c = a[:]  # Neste caso, A LISTA C RECEBE TODOS OS ELEMENTOS DE A (CÓPIA)
b[2] = 8
c[2] = 8
print(f'A lista A: {a}')
print(f'A lista B: {b}')
print(f'A lista C: {c}')

# Definindo 3 pessoas, por meio da estrutura de lista
pessoa1 = ['Pedro', '25']
pessoa2 = ['Maria', '19']
pessoa3 = ['João', '32']
grupoPessoas = []  #Definindo uma var list 'grupoPessoas'
grupoPessoas.append(pessoa1)   #  Inserindo a lista 'pessoa1' dentro da lista 'grupoPessoas'
grupoPessoas.append(pessoa2)   #  Inserindo a lista 'pessoa2' dentro da lista 'grupoPessoas'
grupoPessoas.append(pessoa3)   #  Inserindo a lista 'pessoa3' dentro da lista 'grupoPessoas'

#FORMA SIMPLIFICADA
grupoPessoas = [pessoa1, pessoa2, pessoa3]
print(grupoPessoas)
"""
              GRUPO  PESSOAS
--------------------------------------------------
| [['Pedro', 25] | ['Maria', 19] | ['João', 32]] |   LISTA CONTENDO OUTRAS LISTAS
|     0      1   |   0      1    |  0      1     |
--------------------------------------------------
         0              1              2
"""
print(grupoPessoas[0][0])
print(grupoPessoas[1][1])
print(grupoPessoas[2][0])
print(grupoPessoas[1])
