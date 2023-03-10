import random
randomDeck = [6, 7, 8, 9, 10, 2, 3, 4, 5, 11]

score1 = 0
score2 = 0
times = 0

player1 = score1
player2 = score2

cont = 'да'
while cont == 'да':

    print('Игрок №1')
    while True:
        answer = input('Будешь брть карту?: ')
        if answer == 'да':
            card = random.choice(randomDeck)
            score1 += card
            times += 1
            print('У тебя ', times, ' карты')
        elif answer == 'нет':
            print('У тебя ', score1)
            break
        elif answer != 'да' or 'нет':
            print('Ответь да/нет')
        if score1 > 21:
            print('\nУ тебя ',score1, ', а игра идёт до 21\n\nПобедил Игрок №2')
            exit()

    print('\nИгрок №2')
    while True:
        answer = input('Будешь брть карту?: ')
        if answer == 'да':
            card = random.choice(randomDeck)
            score2 += card
            times += 1
            print('У тебя ', times, ' карты')
        elif answer == 'нет':
            print('У тебя ', score2)
            break
        elif answer != 'да' or 'нет':
            print('Ответь да/нет')
        if score2 > 21:
            print('\nУ тебя ',score2, ', а игра идёт до 21,\n\nПобедил Игрок №1')
            exit()

    if player1 > player2:
        print('У игрока №1 ', score1, ' он победил')
    else:
        print('У игрока №2 ', score2, ' он победил')
cont = input('Хотите сыграть ещё раз?(да/нет): ')