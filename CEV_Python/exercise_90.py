aluno = {'nome': input('Digite o nome do aluno: '), 'média': (float(input('Digite a média do aluno: ')))}

print('=-' * 25)
print(f"O nome do aluno é {aluno['nome']}.")
print(f"Sua média é {aluno['média']}.")
if aluno['média'] < 7:
    aluno['situação'] = 'REPROVADO'
    print(f"Logo, ele está {aluno['situação']}.")
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'RECUPERAÇÃO'
    print(f"Logo, ele está em {aluno['situação']}")
else:
    aluno['situação'] = 'APROVADO'
    print(f"Logo, ele está {aluno['situação']}!")
