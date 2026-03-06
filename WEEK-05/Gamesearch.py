import random

board = [" "] * 9

def show():
    for i in range(0,9,3):
        print(board[i], "|", board[i+1], "|", board[i+2])
    print()

def win(p):
    w = [(0,1,2),(3,4,5),(6,7,8),
         (0,3,6),(1,4,7),(2,5,8),
         (0,4,8),(2,4,6)]
    for a,b,c in w:
        if board[a]==board[b]==board[c]==p:
            return True
    return False

def computer():
    w = [(0,1,2),(3,4,5),(6,7,8),
         (0,3,6),(1,4,7),(2,5,8),
         (0,4,8),(2,4,6)]

    # 1. Try to win
    for a,b,c in w:
        line=[board[a],board[b],board[c]]
        if line.count("O")==2 and line.count(" ")==1:
            move=[a,b,c][line.index(" ")]
            board[move]="O"
            return

    # 2. Block player
    for a,b,c in w:
        line=[board[a],board[b],board[c]]
        if line.count("X")==2 and line.count(" ")==1:
            move=[a,b,c][line.index(" ")]
            board[move]="O"
            return

    # 3. Otherwise random move
    empty=[i for i in range(9) if board[i]==" "]
    if empty:
        board[random.choice(empty)]="O"

while True:
    show()

    pos=int(input("Enter position (1-9): "))-1
    if board[pos]==" ":
        board[pos]="X"

    if win("X"):
        show()
        print("You win!")
        break

    computer()

    if win("O"):
        show()
        print("Computer wins!")
        break

    if " " not in board:
        show()
        print("Draw!")
        break