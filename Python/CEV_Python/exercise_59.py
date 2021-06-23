print('>' * 7, 'Iremos analisar 2 números.', '<' * 7)
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
opcao = 0
print('=-=' * 15)
while opcao != 5:
    print('[1] Somar\n[2] Multiplar\n[3] Descobrir o maior\n[4] Mudar os números\n[5] Sair do programa')
    opcao = int(input('>>>>>Qual sua opção? '))
    print('=-=' * 12)
    if opcao == 1:
        print(f'A soma dos números {num1} e {num2} é: {num1 + num2}.')
    elif opcao == 2:
        print(f'A multiplicação de {num1} por {num2} é: {num1 * num2}.')
    elif opcao == 3:
        if num1 > num2:
            print(f'O número {num1} é maior que {num2}.')
        else:
            print(f'O número {num2} é maior que {num1}.')
    elif opcao == 4:
        num1 = int(input('Digite o primeiro número: '))
        num2 = int(input('Digite o segundo número: '))
    elif opcao == 5:
        print('Encerrando....')
    else:
        print('Opção inválida! Tente novamente.')
    print('=-=' * 12)
