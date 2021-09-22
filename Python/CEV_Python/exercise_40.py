nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2

print(f'\nCom as notas {nota1} e {nota2}, a média do aluno é: {media}.')
if media < 5.0:
    print('O aluno foi reprovado!')
elif 6.9 <= media >= 5.0:
    print('O aluno está em recuperação!')
else:
    print('O aluno está aprovado!')
