frase = str(input('Digite uma frase: ').upper().strip())

if 'A' in frase:
    print(f"A letra 'A' apareceu {frase.count('A')} vezes na frase. ")
    print(f"A primeira letra 'A' aparece na posição {frase.find('A') + 1} .")
    print(f"A última letra 'A' apareceu na posição {frase.rfind('A') + 1} .")
else:
    print("Não há nenhuma letra 'a/A' na frase digitada.")
