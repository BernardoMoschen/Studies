nomeVelho = ''
maisVelho, mulheresNovas, somaIdade, mediaIdade = 0, 0, 0, 0
pess = int(input('Quantas pessoas serão analisadas? '))
for pess in range(1, pess+1):
    print('-' * 7, f'{pess}ª PESSOA', '-' * 7)
    nome = input('Nome: ').title().strip()
    idade = int(input('Idade: '))
    somaIdade += idade
    sexo = input('Sexo [M/F]: ').upper().strip()
    if pess == 1 and sexo == 'M':
        maisVelho = idade
        nomeVelho = nome
    if sexo == 'M' and idade > maisVelho:
        maisVelho = idade
        nomeVelho = nome
    if sexo == 'F' and idade < 20:
        mulheresNovas += 1
mediaIdade = somaIdade / pess
print(f'\nA média da idade do grupo de pessoas analisadas é: {mediaIdade}.')
print(f'O nome do homem mais velho é: {nomeVelho}, pois possui {maisVelho} anos.')
print(f'O total de mulheres com menos de 20 anos é: {mulheresNovas}.')
