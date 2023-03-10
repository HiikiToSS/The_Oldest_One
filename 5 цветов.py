import random
import time
colour = random.choice(['жёлтый', 'белый', 'синий', 'зелёный', 'красный'])
print('Я загадал 1 из 5 цветов')
time.sleep(0.4)
print('Жёлтый, белый, синий, зелёный, красный')
trys = 0
tryagain = True
while tryagain == True:
    time.sleep(0.4)
    choice = input('Как ты думаешь какой цвет я загадал?: ')
    choice = choice.lower()
    if choice == colour:
        print('Ты угадал!')
        tryagain = False
    else:
        if colour == 'жёлтый':
            print('Мне кажется загаданный цвет похож на банан')
        elif colour == 'белый':
            print('Загаданный цвет похож на снег')
        elif colour == 'синий':
            print('Цвет который я загадал цвета моря')
        elif colour == 'зелёный':
            print('Тебе не кается что это может быть зелёный?')
        elif colour == 'красный':
            print('Он как площадь перед кремлём')
    if trys >= 5:
        print('Как ты всё ещё не угадал?! Я загадывал', colour)
        tryagain = False