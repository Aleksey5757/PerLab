import random

colors = ['R', 'G', 'B', 'W']
values = list(range(1, 11))

while True:
    input_ = input("start N C:")
    try:
        N, C = map(int, input_.split())
        if N <= 0 or C <= 0:
            print("N и C должны быть целыми положительными числами")    
        else:
           break
    except ValueError:
        print("N и C должны быть указаны как целые положительные числа.")

koloda = [(color, value) for color in colors for value in values]
random.shuffle(koloda)

players = [koloda[i:i+N] for i in range(0, len(koloda), N)]
while True:
   player_num = int(input('get-cards C (1 до {}): '.format(C)))
   try:
       if player_num == 0:
           print('0 игрока нет')
           break
       elif player_num < 1 or player_num > C:
           print('Нет такого игрока')
       else:
           print('Player {}: '.format(player_num), end="")
           for card in players[player_num-1]:
               print('{}{}'.format(card[0], card[1]), end=" ")
           break
   except ValueError:
       print('Игрок должен быть указан целым числом от 1 до {}.'.format(C))