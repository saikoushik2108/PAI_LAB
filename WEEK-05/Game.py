import math

board = [" "] * 9

def show():
    for i in range(0,9,3):
        print(board[i], board[i+1], board[i+2])
    print()

def win(p):
    w = [(0,1,2),(3,4,5),(6,7,8),
         (0,3,6),(1,4,7),(2,5,8),
         (0,4,8),(2,4,6)]
    for a,b,c in w:
        if board[a]==board[b]==board[c]==p:
            return True
    return False

def minimax(maxp):
    if win("O"): return 1
    if win("X"): return -1
    if " " not in board: return 0

    best = -math.inf if maxp else math.inf

    for i in range(9):
        if board[i]==" ":
            board[i] = "O" if maxp else "X"
            score = minimax(not maxp)
            board[i] = " "
            best = max(best,score) if maxp else min(best,score)

    return best

def computer():
    best = -math.inf
    move = 0
    for i in range(9):
        if board[i]==" ":
            board[i]="O"
            score=minimax(False)
            board[i]=" "
            if score>best:
                best=score
                move=i
    board[move]="O"

while True:
    show()

    pos = int(input("Enter position (1-9): ")) - 1
    if board[pos]==" ":
        board[pos]="X"

    if win("X"):
        show()
        print("You win")
        break

    computer()

    if win("O"):
        show()
        print("Computer wins")
        break

    if " " not in board:
        show()
        print("Draw")
        break