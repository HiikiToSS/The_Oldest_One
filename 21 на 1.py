import random
randomDeck = [6, 7, 8, 9, 10, 2, 3, 4, 5, 11]

score = 0
times = 0

while True:
    answer = input('Будешь брть карту?: ')
    if answer == 'да':
        card = random.choice(randomDeck)
        score += card
        times += 1
        print('У тебя ', times, ' карты')
    elif answer == 'нет':
        print('У тебя ', score)
        break
    elif answer != 'да' or 'нет':
        print('Ответь да/нет')
    if score > 21:
        print('У тебя ',score, ', а игра идёт до 21, ты проиграл')
        break