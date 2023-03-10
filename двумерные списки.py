numbers = [[15,64,92],[54,28,15],[46,62,96]]
string = int(input('Введи номер строки которую хочешь вывести: '))
string-=1
print(numbers[string])
changes = input('Хочешь изменить число в выбранной строке?: ')
if changes == 'да':
    column = int(input('Введи номер столбца который хочешь изменить: '))
    column-=1
    exchange = int(input('Введи число которым хочешь заменить выбранный столбец: '))
    numbers[string][column] = exchange
    print(numbers[string])
elif changes == 'нет':
    print('Хорошего дня')