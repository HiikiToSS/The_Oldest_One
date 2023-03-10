import random
Hangman_pics = ['''
    +---+
        |
        |
        |
      =====
''',
'''
    +---+
    O   |
        |
        |
      =====
''',
'''
    +---+
    O   |
    |   |
        |
      =====
''',
'''
    +---+
    O   |
    | \ |
        |
      =====
''',
'''
    +---+
    O   |
   /|\  |
        |
      =====
''',
'''
    +---+
    O   |
   /|\  |
        |
      =====
''',
'''
    +---+
    O   |
   /|\  |
    /\  |
      =====
''']

words = 'яблоко ананас банан огурец тыква помидор'.split()

def random_word(word_list):
    secretIndex = random.randint(0, len(word_list)-1)
    return word_list[secretIndex]

def display(mistakes, correct, secretWord):
    print(Hangman_pics[len(mistakes)])
    print()
    print('Неверные ответы:', end = '')

    for letter in mistakes:
        print(letter, end = '')
    print()
    blanks = '_' * len(secretWord)          #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    for i in range(len(secretWord)):
        if secretWord[i] in correct:
            blanks = blanks[:i]+secretWord[i] + blanks[i+1:] #!!!!
    for letter in blanks:
        print(letter, end='')

secretWord = random_word(words)
mistakes = ''
correct = ''

gameOver = False
#спрашивает букву

def getGuess(alreadyGuessed):
    while True:
        guess = input('\nВведи букву: ')
        if len(guess) != 1:
            print('Вводить можно только 1 букву')
        elif guess in alreadyGuessed:
            print('Тако ответ уже был')
        elif guess not in 'йцукенгшщзхъфывапролджэёячсмитьбю':
            print('Вводи БУКВЫ')
        else:
            return guess

def playAgain():
    print('Хочешь снова? ')
    return input()

print('ИГРА ВИСЕЛИЦА')

while True:
    display(mistakes, correct, secretWord)
    guess = getGuess(mistakes + correct)
    if guess in secretWord:
        correct+=correct + guess
        for i in range(len(secretWord)):
            if secretWord[i] not in correct:
                allLettersFound = False
                break
        if allLettersFound:
            print('Ты угадал все буквы!')
            gameOver = True
    else: 
        mistakes = mistakes+guess
        if len(mistakes) == len(Hangman_pics)-1:
            display(mistakes, correct, secretWord)
            print('\nGame over!, было загаданно слово', secretWord)
            gameOver = True

    if gameOver:
        if playAgain:
            mistakes = ''
            correct = ''
            gameOver = False
            secretWord = random_word(words)
        else:
            break