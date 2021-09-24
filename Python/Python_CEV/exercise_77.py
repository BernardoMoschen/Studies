palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'PRATICAR'
            'ESTUDAR', 'PERSISTIR', 'TRABALHAR', 'EMPREGO', 'PROGRAMADOR', 'FUTURO')
print('-' * 30)
print(f'{"ANALISADOR DE VOGAIS":^30}')
print('-' * 30)
for p in palavras:
    print(f'\nNa palavra {p} temos: ', end='')
    for letra in p:
        if letra.lower() in 'aàáââeéèêiíìoòóôõuúùû':
            print(letra, end=' ')
