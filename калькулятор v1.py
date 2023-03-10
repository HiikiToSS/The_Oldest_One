cont = 'f'
while cont == 'f':

    what = input('Выбери действие (+, -, /, *, **): ')
    a = float(input('Введи первое число: '))
    b = float(input('Введи второе число: '))

    if what == '+':
        c = a + b
        print('Ответ: ', str(c))

    elif what == '-':
        c = a - b
        print('Ответ: ', str(c))

    elif what == '*':
        c = a * b
        print('Ответ: ', str(c))

    elif what == '/':
        c = a / b
        print('Ответ: ', str(c))

    elif what == '**':
        c = a ** b
        print('Ответ: ', str(c))
    
    else:
        print('Бип-боп, ошибка') 


    cont = input("Press f, if you like math ")
