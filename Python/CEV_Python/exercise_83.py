expr = str(input('Digite uma expressão matemática: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append(simb)
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
print('-=' * 30)
if len(pilha) == 0:
    print('Sua expressão matemática está válida!')
else:
    print('Sua expressão matemática está inválida!')
