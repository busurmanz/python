# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""


# man vs bot

# для того чтобы победить в игре, игроку который будет делать первый ход нужно взять 20 конфет 

import random
from random import randint, choice

print(
    'Candy Game\n'
     'The game involves two players\n'
     'The first move is determined by drawing lots\n'
     'Players move by making a move after each other\n'
     'Rules of the game\n'
     'We have a certain amount of candy\n'
     'In one move, you can pick up no more than 28 candies\n'
     'The one who gets the last candy - lost\n'
 )

messages = ['It, s your turn to take candy', 'Take the candy',
             'how many candies do we take?', 'take more', 'Your move']
max_number_move = 0


def getting_to_know_the_players():
     player1 = input('First player, introduce yourself\n')
     player2 = 'T - 1000'
     print(
         f'Very nice, today you are playing with the terminator T - 1000  {player2}')
     return [player1, player2]


def sweets_game(players):
     global max_number_move
     total_sweets = int(input('Enter how many candies we have in total :\n'))
     max_number_move = int(
         input('Enter the number of candies that can be collected in one turn :\n'))
     first = int(input(
         f'{players[0]}, if you want to go first, press 1, if not, any other key\n'))
     if first != 1:
         first = 0
     return [total_sweets, max_number_move, int(first)]


max_move = max_number_move


def game_player_vs_T_1000(sweets, players, messages):
     global max_number_move
     count = sweets[2]

     while sweets[0] > 0:
         if sweets[0] == (max_number_move and sweets[0] < max_number_move and sweets[0] > 1):
             move = sweets[0] - 1
             print(f'I, m taking {move}')

         elif not count % 2:
             move = random.randint(1, sweets[1])
             print(f'I, m taking {move}')
         else:
             print(f'{players[0]}, {choice(messages)}')
             move = int(input())
             if move > sweets[0] or move > sweets[1]:
                 print(
                     f'You can take no more than {sweets[1]} sweets, we have only {sweets[0]} candies')
                 chance = 2
                 while chance > 0:
                     if sweets[0] >= move <= sweets[1]:
                         break
                     print(f'Try again, you have {chance} attempts')
                     move = int(input())
                     chance -= 1
                 else:
                     return print(f'There are no attempts left. Game over!')
         sweets[0] = sweets[0] - move
         if sweets[0] > 0:
             print(f'Left {sweets[0]} candies')
         else:
             print('All the candies are disassembled.')
         count += 1
     return players[not count % 2]


players = getting_to_know_the_players()
sweets = sweets_game(players)

winer = game_player_vs_T_1000(sweets, players, messages)
if not winer:
     print('We don, t have a winner.')
else:
     print(
         f'Congratulations! This time He won {winer}!He gets all the candy! ')


# man against man


count_of_candies = int(input('Enter the number of candies to play : '))
gamer_1, gamer_2 = input('Enter the name of the first player : '), input(
     'Enter the name of the second player : ')
current_gamer = gamer_1
while count_of_candies > 0:
     print('Number of remaining candies : {}'.format(count_of_candies))
     while True:
         number_to_delete = int(
             input('player, s move {} (take no more than 28 candies) : '.format(current_gamer)))
         if number_to_delete >= 1 and number_to_delete <= 28:
             break
     count_of_candies -= number_to_delete
     current_gamer = gamer_2 if current_gamer == gamer_1 else gamer_1

print('Won => {}' .format(current_gamer))