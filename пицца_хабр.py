import time

cont = 'ы'
while cont == 'ы':

    a = str(input('Какую пиццу хотите заказать(пеперони, маргарита, 4 сыра)?: '))
    b = int(input('Сколько пицц хотите заказать(1, 2, 3...)?: '))
    c = int(input('Сколько сантиметров(25, 33, 44)?: '))

    price_1_25 = 320
    price_1_33 = 390
    price_1_44 = 450

    price_2_25 = 340
    price_2_33 = 410
    price_2_44 = 485
    
    price_3_25 = 375
    price_3_33 = 440
    price_3_44 = 510

    price_4_1 = 1.7
    price_4_2 = 3.65

    if a == "пеперони":
        if c == 25:
            print('К оплате ' + str(price_1_25 * b) + ' рублей')
        elif c == 33:
            print('К оплате ' + str(price_1_33 * b) + ' рублей')
        elif c == 44:
            print('К оплате ' + str(price_1_44 * b) + ' рублей')
        else:
            print("Пиццы нет, но вы держитесь")

    elif a == 'маргарита':
        if c == 25:
            print('К оплате ' + str(price_2_25 * b) + ' рублей')
        elif c == 33:
            print('К оплате ' + str(price_2_33 * b) + ' рублей')
        elif c == 44:
            print('К оплате ' + str(price_2_44 * b) + ' рублей')
        else:
            print("Пиццы нет, но вы держитесь")

    elif a == 'chocolate':
        if c == 25:
            print('О, ты тоже немного любишь шоколад, ну раз немного то бесплатно')
        elif c == 33:
            print('Да ты сладкоежка! С тебя ' + str(price_4_1 * b) + ' евро')
        elif c == 44:
            print('За шоколадку и двор стреляю в упор? С тебя ' + str(price_4_2 * b) + ' евро')
        else:
            if c > int('44'):
                print('Мой повелитель, у нас нет столько запасов')
            elif c < int('44'):
                    print('У нас нету таких шоколадкок, сир')

    elif a == '4 сыра':
        if c == 25:
            print('К оплате ' + str(price_3_25 * b) + ' рублей')
        elif c == 33:
            print('К оплате ' + str(price_3_33 * b) + ' рублей')
        elif c == 44:
            print('К оплате ' + str(price_3_44 * b) + ' рублей')
    else:
        print("Пиццы нет, но вы держитесь")
        
    time.sleep(0.35)
    if a == 'chocolate':
        cont = input("Press ы, если хочешь купить ещё или шоколада (; ")
    else:
        cont = input("Press ы, если хочешь купить ещё пиццы ")