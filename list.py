dish = {}
food1 = input('Введи своё любимое блюдо: ')
dish[1] = food1
food2 = input('Введи своё любимое блюдо: ')
dish[2] = food2
food3 = input('Введи своё любимое блюдо: ')
dish[3] = food3
food4 = input('Введи своё любимое блюдо: ')
dish[4] = food4
print(dish)
wantDel = input('Хочешь убрать какое-то блюдо?: ')
if wantDel == 'да' or 'хочу':
    WhichDelete = int(input('Какое блюдо хочешь убрать? (Введи его номер): '))
    del dish[WhichDelete]
    print(sorted(dish.values()))
elif wantDel != 'да' or 'хочу':
    print('Хорошо')