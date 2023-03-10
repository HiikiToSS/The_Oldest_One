import time

cont = 'ы'
while cont == 'ы':

    print('гречка')
    time.sleep(0.05)
    print('молоко')
    time.sleep(0.05)
    print('яйцо')
    time.sleep(0.05)
    print('манка')
    time.sleep(0.05)
    print('салат айсберг')
    time.sleep(0.05)
    print('сливочное масло')
    time.sleep(0.05)
    print('сосиска')
    time.sleep(0.05)
    print('белый хлеб')
    time.sleep(0.05)
    print('чёрный хлеб')
    time.sleep(0.05)
    print('картошка')
    time.sleep(0.05)
    print('марковь')
    time.sleep(0.05)
    print('капуста')
    time.sleep(0.05)
    print('рис')
    time.sleep(0.05)
    print('курица')
    time.sleep(0.05)
    print('сало')
    time.sleep(0.05)

    #всё на 1 грамм

    buckweat = 3.52 #гречка
    milk = 0.6
    egg = 0.8
    semolina = 3.5 #манка
    salad_ice = 0.14 #айсберг
    butter = 8.84
    sausage = 2.24
    w_bread = 2.65
    d_bread = 2.59 
    potato = 0.77
    carrot = 0.35
    cabbage = 0.25 
    rice = 1.3
    chicken = 2.39
    salo = 4.75

    dish = str(input("Что ел(а)? "))
    weight = input('Сколько грамм? ') #Отсюда убрал float

    if dish == 'сало!':
        if weight == 'много':
            print('Нужно .∆.ø][¥9| сала!!1!1!')
        elif weight != 'много':
            print('Нужно больше сала!!')

    elif dish == 'бульбу':    
        print('Лукашенко одобряет!!')

    elif dish ==  'гречку': #И ещё одна проблема с выдачей else была здесть т.к. здесь вместо elif было if
        print("Калорийность: ", buckweat * float(weight), 'кал.') #Вот здесь (и в остальных таких же местах) было не * float(weight), а просто * weight, но т.к. я убрал тип данных сверху то теперь могу использовать переменную wigth где угодно
        
    elif dish ==  'молоко':
        print("Калорийность: ", milk * float(weight), 'кал.')
        
    elif dish ==  'яйца':
        print("Калорийность: ", egg  * float(weight), 'кал.')
        
    elif dish ==  'манку':
        print("Калорийность: ", semolina * float(weight), 'кал.')
        
    elif dish ==  'салат айсберг':
        print("Калорийность: ", salad_ice * float(weight), 'кал.')
        
    elif dish ==  'сливочное масло':
        print("Калорийность: ", butter * float(weight), 'кал.')

    elif dish ==  'сосиску':
        print("Калорийность: ", sausage * float(weight), 'кал.')
        
    elif dish ==  'белый хлеб':
        print("Калорийность: ", w_bread * float(weight), 'кал.')
        
    elif dish ==  'чёрный хлеб':
        print("Калорийность: ", d_bread * float(weight), 'кал.')
        
    elif dish ==  'картошку':
        print("Калорийность: ", potato * float(weight), 'кал.')
        
    elif dish == 'марковь':
        print('Калорийность', carrot * float(weight), 'кал.')

    elif dish ==  'капусту':
        print('Калорийность: ', cabbage * float(weight), 'кал.')
        
    elif dish ==  'рис':
        print('Калорийность: ', rice * float(weight), 'кал.')
        
    elif dish ==  'курицу':
        print('Калорийность: ', chicken * float(weight), 'кал.')
        
    elif dish == "сало":
        print('Калорийность' , salo * float(weight) , 'кал. ' 'Хохол чё ли?') 

    else:
        print('Неправильно вводишь')
    

    time.sleep(0.35)
    cont = input('нажми ы, что бы продолжить ')