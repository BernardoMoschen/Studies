"""
--->Estruturas Lógicas: and(e), or(ou), not(não), is(é)<---

-->Operadores unários:
    - not, is
-->Operadores binários:
    - and, or

Para o 'and', ambas as condicionais devem ser True.
Pra o 'or', uma ou outra condicional deve ser True.
Para o 'not', o valor booleano é invertido.
Para o 'is', o valor é comparado com um segundo.

"""
# and(e):
ativo = False
logado = True
print('Exemplo de and:')
if ativo and logado:
    print('Bem-vindo usuário!')
else:
    print('Você necessita ativar sua conta para poder entrar no sistema.\nPor favor, cheque seu email.')

# or(ou):
print('\nExemplo de or:')
if ativo or logado:
    print('Bem-vindo usuário!')
else:
    print('Você necessita ativar sua conta para poder entrar no sistema.\nPor favor, cheque seu email.')

# not(não):
print('\nExemplo de not:')
if not ativo:
    print('Bem-vindo usuário!')
else:
    print('Você necessita ativar sua conta para poder entrar no sistema.\nPor favor, cheque seu email.')

# is(é):
print('\nExemplo de is:')
if logado is ativo:
    print('Bem-vindo usuário!')
else:
    print('Você necessita ativar sua conta para poder entrar no sistema.\nPor favor, cheque seu email.')
