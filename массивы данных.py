from array import *
import math

massiv = array('f',[15.37,25.14,45.98,69.38,84.65])
while True:
    number = int(input('Введи число целое от 2 до 5: '))
    if number > 5 or number < 2:
        print('Введи число ОТ 2 ДО 5: ')
    else:
        break

for i in range(5):
    finalResult = massiv[i] / number
    print(round(finalResult, 2))