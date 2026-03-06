import math

board = [" "] * 9

def show():
    for i in range(0,9,3):
        print(board[i], "|", board[i+1], "|", board[i+2])
    print()

def win(p):
    w = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    return any(board[a]==board[b]==board[c]==p for a,b,c in w)

def minimax(is_max, alpha, beta):
    if win("O"): return 1
    if win("X"): return -1
    if " " not in board: return 0
    if is_max:
        best=-math.inf
        for i in range(9):
            if board[i]==" ":
                board[i]="O"
                best=max(best,minimax(False,alpha,beta))
                board[i]=" "
                alpha=max(alpha,best)
                if beta<=alpha: break
        return best
    else:
        best=math.inf
        for i in range(9):
            if board[i]==" ":
                board[i]="X"
                best=min(best,minimax(True,alpha,beta))
                board[i]=" "
                beta=min(beta,best)
                if beta<=alpha: break
        return best

def computer():
    best_score=-math.inf
    move=0
    for i in range(9):
        if board[i]==" ":
            board[i]="O"
            score=minimax(False,-math.inf,math.inf)
            board[i]=" "
            if score>best_score:
                best_score=score
                move=i
    board[move]="O"

while True:
    show()
    pos=int(input("Enter position (1-9):"))-1
    if board[pos]==" ":
        board[pos]="X"
    if win("X"):
        show(); print("You win!"); break
    computer()
    if win("O"):
        show(); print("Computer wins!"); break
    if " " not in board:
        show(); print("Draw!"); break