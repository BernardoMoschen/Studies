from datetime import date
print('---Consultor de Alistamento Militar---')
sexo = input("Digite seu sexo, 'M' para homem ou 'F' para mulher, de acordo com seu RG.\n")

if sexo == 'F' or sexo == 'f':
    print('Seu alistamento não é obrigatório.')
    alistar = input("Se você deseja se alistar, digite 'S', ou, digite 'N' para encerrar o programa.\n")
    if alistar == 'S' or alistar == 's':
        anoNascimento = int(input('Digite seu ano de nascimento: '))
        anoAtual = date.today().year
        idade = anoAtual - anoNascimento
        print(f'\nVocê está com {idade} anos.')

        if idade < 18:
            print(f'\nAinda faltam {18 - idade} ano(s) para seu alistamento.')
            print(f'Seu alistamento será em {anoAtual + (18 - idade)}.')
        elif idade > 18:
            print(f'Já deveria ter se alistado em {idade - 18}.')
            print(f'Seu alistamento foi em {anoAtual - (idade - 18)}.')
        else:
            print('É o ano do seu alistamento, procure realizá-lo imediatamente!')

    elif alistar == 'N' or alistar == 'n':
        print('Você escolheu sair.')
