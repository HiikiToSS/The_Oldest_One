a = 1
while a == 1:
    name = input('введи слово ')
    times = int(input('введи кол-во раз вывода слова '))

    if times < 10:
        for z in range(times):
            print(name)

    elif times > 10:
            print('слишком много')