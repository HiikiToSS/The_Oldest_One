import random
def twoNums():
    stNum = int(input('Введи 1е число: '))
    ndNum = int(input('Введи 2е число: '))
    compNum = random.randint(stNum, ndNum)
    return compNum

def answer():
    print('Thinking of number... ')
    answer = int(input('Как ты думаешь какое число я выбрал?: '))
    return answer

def correctAns(answer, compNum):
    tryAgain = True
    while tryAgain == True:
        if answer == compNum:
            print('Верно, ты угадал!')
            tryAgain = False
        elif answer > compNum:
            answer = int(input('Больше загаданного, попробуй ещё раз: \n'))
        else:
            answer = int(input('Меньше загаданного, попробуй ещё раз: \n'))

compNum = twoNums()
answer = answer()
correctAns(answer, compNum)