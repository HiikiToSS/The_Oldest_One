import random
import time

while a == 'n':
    guess = input('Как ты думаешь что выпадет (О)рёл или (Р)ешка?: ')
    print('Подбрасываю монетку... ')
    time.sleep(2.5)
    coin = random.choice(['орёл', 'решка'])
    if guess == coin:
        if coin =='орёл':
            print('Ты угадал выпал орёл')
        elif coin =='решка':
            print('Ты угадал, выпала решка')
    elif guess != coin:
        if coin =='орёл':
            print('Ты не угадал выпал орёл')
        elif coin =='решка':
            print('Ты не угадал, выпала решка')
    else: print('Выбери орла или решку')
    a = input('Хочешь подбросить монетку ещё раз? (y/n)')
    if a == 'n':
        print('Ну нет так нет')