"""
---> Recebendo dados do usuário <---

input() -> Todo dado recebido via input é do tipo String.

Em Python, string é tudo que estiver entre:
- Aspas simples;
- Aspas duplas;
- Aspas simples triplas;
- Aspas duplas triplas;

Exemplos:
- Aspas simples -> 'Angelina Jolie'
- Aspas duplas ->  "Angelina Jolie'
- Aspas simples triplas -> '''Angelina Jolie'''
- Aspas duplas triplas -> (Todo esse comentário).
"""
#Entrada de dados
print('Qual seu nome ?')
nome = input()


# Saída de dados
# ->Exemplo de print 'antigo' Python 2.x :
# print('Seja bem-vindo(a) %s' %nome)


# ->Exemplo de print 'anterior' Python 3.x :
# print('Seja bem-vindo(a) {0}'.format(nome))

# ->Exemplo de print 'mais atual' Python 3.7 :
print(f'Seja bem vindo(a) {nome}.')


# Entrada de dados
# ->Forma extensa:
#print("Qual sua idade?")
#idade = input()

# ->Forma Simplificada:
#idade = input('Qual sua idade?')

# ->Forma Simplificada já com cast aplicado, otimizando código:
idade = int(input('Qual sua idade?'))


# Processamento

# Saída
# ->Exemplo de print 'antigo' Python 2.x :
# print('A %s tem %s anos' % (nome, idade))

# ->Exemplo de print 'anterior' Python 3.x :
#print ('A {0} tem {1} anos'.format(nome,idade))

# ->Exemplo de print 'mais atual' Python 3.7 :
print(f'O/A {nome} tem {idade} anos.')

"""
#int(idade) => cast
Cast é a 'conversão' de um tipo de dado para outro.
"""
#print(f'A {nome} nasceu em {2018 - int(idade)}')

#Saída simplificada (cast já aplicado no input):
print(f'O/A {nome} nasceu em {2021 - (idade)}.')
