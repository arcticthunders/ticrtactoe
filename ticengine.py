from collections import Counter
import random as r
BOARD_WIDTH = 3
BOARD_HEIGHT = 3

referance = [1,2,3,4,5,6,7,8,9]

def randomAi(board):
        x,y = r.randint(0,2), r.randint(0,2)
        return(x,y)


def winningMove(board, playerFlag):
    if(playerFlag == True):
        player = 'X'
        enemy ='O'
    else:
        player = 'O'
        enemy ='X'
    columns = rows(board)
    for c in columns:
        countPlayer = Counter(c)[player]
        countEnemy = Counter(c)[enemy]
        if(countPlayer == 2 and countEnemy == 0):
            for i in range(3):
                if(c[i] not in ['X','O']):
                    return c[i]
    return None

def newBoard():
    board = []
    count = 1
    for i in range(BOARD_WIDTH):
        column =[]
        for j in range(BOARD_HEIGHT):
            column.append(count)
            count += 1
        board.append(column)
    return board


def render(board):
    rows  = []
    for y in range(BOARD_HEIGHT):
        row = []
        for x in range(BOARD_WIDTH):
            row.append(board[x][y])
        rows.append(row)
    i = 0
    for r in rows:
        printable = ' '
        for element in r:
                printable += str(element) + ' '
        print( printable)
        i += 1


def makeMove(board, player, move):
    if(board[move[0]][move[1]] not in referance):
        print("illegal move! Try Again!!")
        return False
    else:
        board[move[0]][move[1]] = player
        return True


def rows(board):
    rows = []
    for i in range(3):
        rows.append(board[i][:])
        row = []
        for j in range(3):
            row.append(board[j][i])
        rows.append(row)
    row = []
    row.append(board[0][0])
    row.append(board[1][1])
    row.append(board[2][2])
    rows.append(row)
    row = []
    row.append(board[0][2])
    row.append(board[1][1])
    row.append(board[2][0])
    rows.append(row)
    return rows


def win(rows):
    for r in rows:
        count = Counter(r)
        countX = count['X']
        countO = count['O']
        if(countX == 3):
            return ('X' ,True)
        if(countO == 3):
            return ('O' ,True)
    return (None,False)


playerFlag = True
count = 1
board = newBoard()
print("board created")
render(board)
print("player 1 is 'X' , player 2 is 'O' ")
while(count):
        status = False
        count += 1
        while(not status):
            winGame = winningMove(board, playerFlag)
            if(winGame != None):
                print('Play at:' + str(winGame))
            enter = input('press enter to continue')
            (x,y) = randomAi(board)
            if(playerFlag == True):
                status = makeMove(board, 'X', [x,y])
            else:
                status = makeMove(board, 'O', [x,y])
            playerFlag = not playerFlag
            render(board)
            columns = rows(board)
            (winner  ,winStatus) = win(columns)
            if(winStatus == True):
                print("There is winner :" + winner)
                count = 0
                break
        if(count == 10):
            print("it is a draw")
            count = 0
            break
