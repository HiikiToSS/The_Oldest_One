cont = 'f'
while cont == 'f':

    a = str(input('какое мароженное хотите купить(пломбир, шоколадное, фисташковое, клубничное)?: '))
    b = int(input('сколько мароженных хотите купить(1, 2, 3...)?: '))
    c = str(input('стаканчик или рожок ?: '))

    plom_st = 45
    plom_ro = 60
    
    choco_st = 38
    choco_ro = 52
    
    ber_st = 42
    ber_ro = 58
    
    fist_st = 46
    fist_ro = 62

    if a == "пломбир":
        if c == 'стаканчик':
            print('К оплате ' + str(plom_st * b) + ' рублей')
        elif c == 'рожок':
            print('К оплате ' + str(plom_ro * b) + ' рублей')
        else:
            print("На улице жара, всё раскупили")

    elif a == 'шоколадное':
        if c == 'стаканчик':
            print('К оплате ' + str(choco_st * b) + ' рублей')
        elif c == 'рожок':
            print('К оплате ' + str(choco_ro * b) + ' рублей')
        else:
            print("На улице жара, всё раскупили")

    elif a == 'фисташковое':
        if c == 'стаканчик':
            print('К оплате ' + str(fist_st * b) + ' рублей')
        elif c == 'рожок':
            print('К оплате ' + str(fist_ro * b) + ' рублей')
        else:
            print("На улице жара, всё раскупили")
        
    elif a == 'клубничное':
        if c == 'стаканчик':
            print('К оплате ' + str(ber_st * b) + ' рублей')
        elif c == 'рожок':
            print('К оплате ' + str(ber_ro * b) + ' рублей')
    else:
        print("На улице жара, всё раскупили")

    import time
    time.sleep(0.35)

    cont = input("Press f, чтобы купить больше мороженного ")
