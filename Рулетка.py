import random
import time
print('\nwww.AZINO777.bigWin.com')
wallet = 107
wheel = ['7','кокос','ананас']

print('Баланс ', wallet, ' рублей')

while True:
    spin = input('Вращать рулетку?: ')
    if spin == 'да':
        band1 = random.choice(wheel)
        band2 = random.choice(wheel)
        band3 = random.choice(wheel)
        print(band1)
        time.sleep(0.3)
        print(band2)
        time.sleep(0.3)
        print(band3)
        wallet -= 15
        if band1 == band2 == band3 == '7':
            wallet += 69
            print('\nJaCKPOT!!\n')
            time.sleep(2)
        elif band1 == band2 == band3 == 'ананас' or band1 == band2 == band3 == 'кокос':
            wallet += 43
            print('\nMiINIWIN\n')
            time.sleep(2)
        elif band1 == band2  == 'кокос' or band1 == band3  == 'кокос' or band2 == band3  == 'кокос' or band1 == band2  == 'ананас' or band1 == band3  == 'ананас' or band2 == band3  == 'ананас':
            wallet += 7
        elif band1 == band2  == '7' or band1 == band3  == '7' or band2 == band3  == '7':
            wallet += 17
        print('Баланс ', wallet, ' рублей\n')
    else:
        if wallet > 107:
            print('Ты везунчик, приходи ещё')
        elif wallet < 107:
            print('Тебе же почти выпал джекпот, просто иди продай почку и покрути ещё!')
        break
    if wallet <= 0:
        print('Ваш баланс на нуле, приходите завтра')
        break