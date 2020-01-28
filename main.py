def printHead():
    print('+-------+-------+-------+')
    
def printRow(row):
    print('|       |       |       |')
    print('|   {0}   |   {1}   |   {2}   |'.format(row[0], row[1], row[2]))
    print('|       |       |       |')
    print('+-------+-------+-------+')
    
def DisplayBoard(board):
    printHead()
    for i in range(len(board)):
        printRow(board[i])
    
#
# the function accepts one parameter containing the board's current status
# and prints it out to the console
#

def printBadInput():
     print("Bad input")

def getAddress(index):
    row = index //3
    col = index %3
    return (row, col)
    
def valByIndex(board, index):
    a = getAddress(index)
    r,c = a
    return board[r][c]

def EnterMove(board):
    userInput = input("Enter your move: ")
    try:
        userInput = int(userInput)
    except ValueError:
        printBadInput()
        return
    if not userInput <9:
        printBadInput()
        return
    val = valByIndex(board, userInput)
    if type(val)==type(1):
        r,c = getAddress(userInput)
        board[r][c] = 'O'
    else:
        printBadInput()
        
#
# the function accepts the board current status, asks the user about their move, 
# checks the input and updates the board according to the user's decision
#

def MakeListOfFreeFields(board):
    ret = []
    for r in range(3):
        for c in range(3):
            if type(board[r][c])==type(1):
                ret.append((r,c))
    return ret
#
# the function browses the board and builds a list of all the free squares; 
# the list consists of tuples, while each tuple is a pair of row and column numbers
#

def checkDiag1(board, sign):
    if board[0][0]==sign and \
       board[1][1]==sign and \
       board[2][2]==sign :
        return True
    else:
        return False

def checkDiag2(board, sign):
    if board[0][2]==sign and \
       board[1][1]==sign and \
       board[2][0]==sign :
        return True
    else:
        return False

def checkRow(board, index, sign):
    if board[index][0]==sign and \
       board[index][1]==sign and \
       board[index][2]==sign :
        return True
    else:
        return False
        
def checkCol(board, index, sign):
    if board[0][index]==sign and \
       board[1][index]==sign and \
       board[2][index]==sign :
        return True
    else:
        return False
        
def VictoryFor(board, sign):
    res = checkDiag1(board, sign) or checkDiag2(board, sign) \
         or checkRow(board, 0, sign) or checkRow(board, 1, sign) or checkRow(board, 2, sign) \
         or checkCol(board, 0, sign) or checkCol(board, 1, sign) or checkCol(board, 2, sign)
    return res
#
# the function analyzes the board status in order to check if 
# the player using 'O's or 'X's has won the game
#

from random import randrange

def DrawMove(board):
    frees = MakeListOfFreeFields(board)
    target = frees[randrange(len(frees))]
    r,c = target
    board[r][c] = 'X'
#
# the function draws the computer's move and updates the board
#

board = [[i, i+1, i+2] for i in range(0,9,3)]
board[1][1] = 'X'

DisplayBoard(board)

iteration = 0
while True:
    EnterMove(board)
    iteration += 1
    DisplayBoard(board)
    if VictoryFor(board, 'O'):
      print("You won!")
      break

    DrawMove(board)
    iteration +=1
    DisplayBoard(board)
    if VictoryFor(board, 'X'):
      print("I won, you sucker!")
      break
    if iteration == 8:
      print("Dead heat, try again")
      break
