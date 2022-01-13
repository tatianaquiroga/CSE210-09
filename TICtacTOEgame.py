#W02 Prove: Developer - Solo Code Submission
# Student : Tatiana Andrea Quiroga Meza
#CSE210 - Team 09


print("This is a TIC-TAC-TOE game.")
print("This are the positions to play")
print("__________________")
print ("| ","1 ","| ","2 ","| ","3 ","|")
print("|-----+-----+-----|")
print ("| ","4 ","| ","5 ","| ","6 ","|")
print("|-----+-----+-----|")
print ("| ","7 ","| ","8 ","| ","9 ","|")
print("___________________")
print()

#We create the board
def print_board(board):
    for i in range(0,7,3):
        print(board[i] + " | " + board[i+1] + " | " + board[i+2])

board= [""]*9

#we create an ending parameter to the game
gFinish = False
#We create a value to turn player
turnX = True

while not gFinish:
    #possible play, no replace movement
    possible_play = False
    while not possible_play:
        try:
            pos=int(input("Please Choose a position to play between 1 and 9:  "))
            if board[pos -1] == "":
                possible_play = True
            else:
                print("Somebody already play there, ")
                print("Choose another position between 1 and 9: ")
        except:
            print("No such a movement")
    #change turn
    board[pos -1] = "x" if turnX else "o"

    print_board(board)

    #We define a winner

if (board[0] == board[1] == board[2] and board[0] != "" or 
    board[3] == board[4] == board[5] and board[0] != "" or
    board[6] == board[7] == board[8] and board[6] != "" or
    board[0] == board[3] == board[6] and board[0] != "" or
    board[1] == board[4] == board[7] and board[1] != "" or
    board[2] == board[5] == board[8] and board[2] != "" or
    board[0] == board[4] == board[8] and board[0] != "" or
    board[2] == board[4] == board[6] and board[0] != "" ):
        print("The winner is: " + "x" if turnX else "The winner is: " + "o")
        gFinish == True
        
    #in Draw
    
if "" not in board:
    print("No winner")
    print("Good game. Thanks for playing!")
    gFinish = True

turnX = not turnX



