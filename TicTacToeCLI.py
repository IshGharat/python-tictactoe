import numpy as np

ROWS=3
COLUMNS=3

def mark(row,col,player):
    board[row][col]=player

def is_valid_mark(row,col):
    return board[row][col]==0

def is_board_full():
    for c in range(COLUMNS):
        for r in range(ROWS):
            if board[r][c]==0:
                return False
    return True

def is_winning_move(player):
    if player ==1:
        winner="Player 1 won"
    else:
        winner="Player 2 won"

    for r in range(ROWS):
        if board[r][0]==player and board[r][1]==player and board[r][2]==player:
            print(winner)
            return True
    
    for c in range(COLUMNS):
        if board[0][c]==player and board[1][c]==player and board[2][c]==player:
            print(winner)
            return True
    
    if board[0][0]==player and board[1][1]==player and board[2][2]==player:
        print(winner)
        return True
    
    if board[0][2]==player and board[1][1]==player and board[2][0]==player:
        print(winner)
        return True

        

board=np.zeros((ROWS,COLUMNS))

game_over=False
Turn=0

while not game_over:
    if(Turn%2==0):
        #Player 1
        row=int(input("Player 1: Choose row number(0-2): "))
        col=int(input("Player 1: Choose column number(0-2): "))

        if is_valid_mark(row,col):
            mark(row,col,1)
            if is_winning_move(1):
                game_over=True
        else:
            Turn-=1
    else:
        #Player 2
        row=int(input("Player 2: Choose row number(0-2): "))
        col=int(input("Player 2: Choose column number(0-2): "))

        if is_valid_mark(row,col):
            mark(row,col,2)
            if is_winning_move(2):
                game_over=True
        else:
            Turn-=1

    Turn+=1
    print(board)
    if game_over==True:
        print("Game over")





