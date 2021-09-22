futebolista = {'Nome': input('Nome do jogador: '),
               'gols': [],
               'total': 0}
partidas = int(input(f'Quantas partidas {futebolista["Nome"]} jogou? '))
for i in range(1, partidas + 1):
    futebolista['gols'].append(int(input(f'Quantos gols na {i}º partida? ')))
futebolista['total'] += sum(futebolista['gols'])
print('=-' * 30)
print(futebolista.items())
print('=-' * 30)
for k, v in futebolista.items():
    print(f'O campo {k} tem o valor {v}.')
print('=-' * 30)
print(f'O jogador {futebolista["Nome"]} jogou {partidas} partidas.')
for i in range(0, len(futebolista['gols'])):
    print(f"    => Na {i + 1}º partida, fez {futebolista['gols'][i]} gols.")
print(f'Foi um total de {futebolista["total"]} gols!')
