#nathan broadbent
#12/18

#global constraints
X="X"
O="O"
EMPTY=" "
TIE="TIE"
NUM_SQUARES=9
# first function
def display_instructions():
    print("""welcome to the tic tac toe player

you will be shown a board of nine spaces you can play on any space that is not open
0-8 get three x's or o's in a row to win

                0 |  1  | 2
                ------
                3 | 4 | 5
                ------
                6 |  7 | 8
                
time to lose monkey spawn
""")
#second function
def ask_yes_no(question):
    response=None
    while response not in ("y","n"):
        response=input(question+" y or n").lower()
    return response
#third function
def ask_num(question,low,high):

    response="9999"
    while True:
        if response.isdigit():
            if int(response) in range(low,high):
                break
            else:
                response=input(question)
        else:
            print("enter a number")
            response=input(question)
    return int(response)
#fourth function
def pieces():
    go_first=ask_yes_no("would you like to go first")
    if go_first=="y":
        print("rushing to your doom")
        humanPiece=X
        computerPiece=O
    else:
        print("you coward")
        humanPiece=O
        computerPiece=X
    return humanPiece,computerPiece
#fifth function
def new_board():
    board=[]
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board
#sixth function
def display_board(board):
    print("\n\t",board[0],"|",board[1],"|",board[2])
    print("\t","------")
    print("\t",board[3],"|",board[4],"|",board[5])
    print("\t","------")
    print("\t",board[6],"|",board[7],"|",board[8],"\n")
#seventh function
def legal_moves(board):
    moves=[]
    for square in range(NUM_SQUARES):
        if board[square]==EMPTY:
            moves.append(square)
    return moves
#eighth function
def winner(board):
    WAYS_TO_WIN=((0,1,2),
                 (3,4,5),
                 (6,7,8),
                 (0,3,6),
                 (1,4,7),
                 (2,5,8),
                 (0,4,8),
                 (2,4,6))
    for row in WAYS_TO_WIN:
        if board[row[0]]==board[row[1]]==board[row[2]]!=EMPTY:
            winner=board[row[0]]
            return winner
    if EMPTY not in board:
         return TIE
    return None
#NINTH FUNCTION
