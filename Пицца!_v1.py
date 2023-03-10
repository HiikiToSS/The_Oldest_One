cont = 'f'
while cont == 'f':
    a = float(input('Сколько стоит пицца? '))
    b = float(input('Сколько % скидка? '))
    c = a / 100 * b
    d = a - c
    print('Пицца стоит ' + str(round(d)) + ' рублей')
    cont = input("Press f, что бы узнать стоимость еще 1 пиццы")
