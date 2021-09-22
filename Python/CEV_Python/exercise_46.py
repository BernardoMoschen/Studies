from time import sleep
contagem = int(input('Digite a quantidade de segundos para a contagem: '))
for i in range(contagem, 0, -1):
    print(i)
    sleep(1)
print('Acabou !')
