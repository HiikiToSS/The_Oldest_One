import random

def drawBoard ():
    print('   |   |')
    print(' ', board[7] ,'|' , board[7], '|',  board[7], '|')
    print('   |   |')
    print('---+---+---')
    print('   |   |')
    print(' ', board[4] ,'|' , board[5], '|',  board[6], '|')
    print('   |   |')
    print('---+---+---')
    print('   |   |')
    print(' ', board[1] ,'|' , board[2], '|',  board[3], '|')

def PlayerLetter():
    letter = ''
    while not letter == 'x' or '0':
        letter = input('Введи крестик (х) или нолик (0):\n ').upper()
        if letter == 'X':
            return['X', 'O']
        else:
            return ['O', 'X']

def stMove():
    if random.choice(0,1) ==0:
        return 'computer'
    else:
        return 'игрок'        

def playAgain():
    return input('Хочешь сыграть снова?: ').lower().startswith('да')

def makeMove(board, letter, move):
     board[move] = letter

def isWinner(board, letter):
    return ((board[7]==letter and board[8]==letter and board[9]==letter)
     or (board[1]==letter and board[2]==letter and board[3]==letter)
     or (board[4]==letter and board[5]==letter and board[6]==letter)
     or (board[7]==letter and board[5]==letter and board[3]==letter)
     or (board[9]==letter and board[5]==letter and board[1]==letter)
     or (board[9]==letter and board[6]==letter and board[3]==letter)
     or (board[8]==letter and board[5]==letter and board[2]==letter)
     or (board[7]==letter and board[4]==letter and board[1]==letter))

def cleanPlace (board, move):
    return board[move] == ''

def playerMove(board):
    move = ''
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not cleanPlace(board, move):
        move = int(input('Ваш ход (1-9)'))
        return move