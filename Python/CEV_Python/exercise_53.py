frase = input('Digite uma frase: ').strip().upper()
palavras = frase.split()
juntas = ''.join(palavras)
reverse = juntas[::-1]
print(f"\nO reverso de '{frase}' é '{reverse}'.")
if reverse == juntas:
    print('A frase \033[32mé \033[mum \033[32mPALÍNDROMO!')
else:
    print('A frase \033[31mNÃO \033[mé um \033[31mPALÍNDROMO!')
