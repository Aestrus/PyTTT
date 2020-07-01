# Python Tic-Tac-Toe

'''
- Menu screen to start game (name players, player 1 always starts first)
- Create the board
- Recursively insert into board until a player wins or until no pieces are left.
        - Make sure selected placement is valid before placing.
            - If it is valid, place piece and then move to next step.
            - If it is not valid, output that it is invalid and let the player choose again.       
        - Check state after every turn before moving forward.
            - If it is still winnable for either player, continue.
            - If it is not winnable for either player, end game with a draw.
- Once game is complete, display fancy win or draw screen.
        - Include "Menu" and "Quit" options after game end.
            - If nothing is chosen within 15 seconds, automatically quit. Make sure to display that you will be doing this somewhere.
'''

from board import buildBoard

# Have a module for board manipulation
# Current program is driver program

def startGame():
    print("Starting the game.")
    playerOne = input('What is player 1\'s name?')
    playerTwo = input('What is player 2\'s name?')
    initBoard = buildBoard()
    currPlayerPiece = "x"

    # TODO: while(stateCheck(initBoard, currPlayerPiece) == False):


    return
    

# Menu Screen
print("Welcome to Tic Tac Toe built in Python!")
option = input('Type "start" when you are ready to begin! Otherwise, type "quit" if you want to exit the program.')

if option == "start" or option == "Start":
    startGame()

elif option == "quit" or option == "Quit":
    print("Quitting the program....")
    quit
else:
    print("Invalid answer. Quitting the program.")
    quit

