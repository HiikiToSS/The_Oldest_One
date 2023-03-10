import math

cont = 'f'
while cont == 'f':

    what = input('Выбери действие(+, -, /, *, **,)? ')
    if what == '':
        print("Как ты сломал калькулятор?")
        break
    if what == '+':
        a = float(input('К чему будем прибавлять? : '))
        b = float(input('Сколько будем прибавлять? : '))
    elif what == '-':
        a = float(input('Из скольки будем вычитать? : '))
        b = float(input('Сколько будем вычитать? : '))
    elif what == '/':
        a = float(input('Что будем делить? : '))
        b = float(input('На что будем делить? : '))
    elif what == '*':
        a = float(input('Что будем умножать? : '))
        b = float(input('На что будем умножать? : '))
    elif what == '**':
        a = float(input('Что будем возводить в степень? : '))
        b = float(input('В какую степень будем возводить? : '))
    
    d = str(input('Будем округлять? '))
    if d == 'да':
        e = str(input("В большую, меньшую сторону или ни в какую? "))

    if what == '+':
        if d == 'да':
            if e == 'в большую':
                c = a + b
                print('Ответ: ', int(c))
            if e == 'в меньшую':
                c = a + b
                print ('Ответ: ', math.floor(c))
            if e == 'ни в какую':
                c = a + b
                print('Ответ: ', round(c))
        elif d == 'нет':
            c = a + b
            print('Ответ: ', c)
        else:
            print("Как ты сломал калькулятор?")

    elif what == '-':
        if d == 'да':
            if e == 'в большую':
                c = a - b
                print('Ответ: ', int(c))
            if e == 'в меньшую':
                c = a - b
                print('Ответ: ', math.floor(c))
            if e == 'ни в какую':
                c = a - b
                print('Ответ: ', round(c))
        elif d == 'нет':
            c = a - b
            print('Ответ: ', c)
        else:
            print("Как ты сломал калькулятор?")

    elif what == '/':
        if d == 'да':
            if e == 'в большую':
                c = a / b
                print('Ответ: ', int(c))
            if e == 'в меньшую':
                c = a / b
                print ('Ответ: ', math.floor(c))
            if e == 'ни в какую':
                c = a / b
                print('Ответ: ', round(c))
        elif d == 'нет':
            c = a / b
            print('Ответ: ', c)
        else:
            print("Как ты сломал калькулятор?")

    elif what == '*':
        if d == 'да':
            if e == 'в большую':
                c = a * b
                print('Ответ: ', int(c))
            if e == 'в меньшую':
                c = a * b
                print ('Ответ: ', math.floor(c))
            if e == 'ни в какую':
                c = a * b
                print('Ответ: ', round(c))
        elif d == 'нет':
            c = a * b
            print('Ответ: ', c)
        else:
            print("Как ты сломал калькулятор?")

    elif what == '**':
        if d == 'да':
            if e == 'в большую':
                c = a ** b
                print('Ответ: ', int(c))
            if e == 'в меньшую':
                c = a ** b
                print ('Ответ: ', math.floor(c))
            if e == 'ни в какую':
                c = a ** b
                print('Ответ: ', round(c))
        elif d == 'нет':
            c = a ** b
            print('Ответ: ', c)
        else:
            print("Как ты сломал калькулятор?")
            
    import time
    time.sleep(0.35)
    cont = input("Press f, if you like math ")
