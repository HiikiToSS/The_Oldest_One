import random
print('Угадай число от 1 до 12')
trys = int(input('сколько попыток хочешь?: '))
rand = random.randint(1, 12)
print(rand)
for i in range(trys, 0, -1):
    pop = int(input('Угадай число: '))
    if pop > 12:
        print('Написано же ДО 12')
        break
    elif pop < 0:
        print('Написано же ОТ 0')
        break
    if pop == rand:
        print()
        print('Правильно! Было загадано ', rand, '!')
        break
    elif pop != rand:
        if pop > rand:
            print('Не угадал, осталось ', i -1, " попыток, загаданное число меньше выбранного")
        elif pop < rand:
            print('Не угадал, осталось ', i -1, " попыток, загаданное число больше выбранного")