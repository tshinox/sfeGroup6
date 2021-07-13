#Tic Tac Toe game in python by techwithtim

board = [' ' for x in range(10)]

def insertLetter(letter, pos):
    board[pos] = letter

def spaceIsFree(pos):
    return board[pos] == ' '

def printBoard(board):
    print('-------------')
    print('| ' + board[1] + ' | ' + board[2] + ' | ' + board[3]+ ' | ')
    print('-------------')
    print('| ' + board[4] + ' | ' + board[5] + ' | ' + board[6]+ ' | ')
    print('-------------')
    print('| ' + board[7] + ' | ' + board[8] + ' | ' + board[9]+ ' | ')
    print('-------------')
    
    
def isWinner(bo, le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or(bo[1] == le and bo[2] == le and bo[3] == le) or(bo[1] == le and bo[4] == le and bo[7] == le) or(bo[2] == le and bo[5] == le and bo[8] == le) or(bo[3] == le and bo[6] == le and bo[9] == le) or(bo[1] == le and bo[5] == le and bo[9] == le) or(bo[3] == le and bo[5] == le and bo[7] == le)

def player1Move():
    run = True
    while run:
        row = int(input('Player X, please enter a row (0, 1 or 2): '))
        col = int(input('Player X, please enter a column (0, 1 or 2): '))
        if row == 0 and col == 0:
            move = 1
        elif row == 0 and col == 1:
            move = 2
        elif row == 0 and col == 2:
            move = 3
        elif row == 1 and col == 0:
            move = 4
        elif row == 1 and col == 1:
            move = 5
        elif row == 1 and col == 2:
            move = 6
        elif row == 2 and col == 0:
            move = 7
        elif row == 2 and col == 1:
            move = 8
        elif row == 2 and col == 2:
            move = 9
        else:
            print('Invalid row or column value')

        try:
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print('Sorry, this space is occupied!')
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number!')

def player2Move():
    run = True
    while run:
        row = int(input('Player O, please enter a row (0, 1 or 2): '))
        col = int(input('Player O, please enter a column (0, 1 or 2): '))
        if row == 0 and col == 0:
            move = 1
        elif row == 0 and col == 1:
            move = 2
        elif row == 0 and col == 2:
            move = 3
        elif row == 1 and col == 0:
            move = 4
        elif row == 1 and col == 1:
            move = 5
        elif row == 1 and col == 2:
            move = 6
        elif row == 2 and col == 0:
            move = 7
        elif row == 2 and col == 1:
            move = 8
        elif row == 2 and col == 2:
            move = 9
        else:
            print('Invalid row or column value')

        try:
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('O', move)
                else:
                    print('Sorry, this space is occupied!')
            else:
                print('Please type a number within the range!')
        except:
            print('Please enter row and column value!')
              

def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def main():
    print('Welcome to Tic Tac Toe!')
    printBoard(board)

    while not(isBoardFull(board)):
        if not(isWinner(board, 'O')):
            player1Move()
            printBoard(board)
        else:
            print('Sorry, O\'s won this time!')
            break

        if not(isWinner(board, 'X')):
            player2Move()
           # if move == 0:
           #     print('Tie Game!')
           # else:
            printBoard(board)
        else:
            print('X\'s won this time! Good Job!')
            break

    if isBoardFull(board):
        print('Tie Game!')

while True:
    answer = input('Do you want to play again? (Y/N)')
    if answer.lower() == 'y' or answer.lower == 'yes':
        board = [' ' for x in range(10)]
        print('-----------------------------------')
        main()
    else:
        break