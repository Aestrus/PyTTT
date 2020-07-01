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

import board

# Have a module for board manipulation
# Current program is driver program

def startGame():
    print("\nStarting the game.")
    playerOne = input('What is player 1\'s name? ')
    playerTwo = input('What is player 2\'s name? ')
    initBoard = board.buildBoard()
    currPlayerPiece = "X"
    col = 0
    row = 0
    placement = [0, 0]
    i = 0

    # While no victory is achieved, continue playing the game.
    # State is checked after each turn.
    while(board.stateCheck(initBoard, currPlayerPiece) == False):
        # Designate next player
        if currPlayerPiece == 'X':
            currPlayerPiece = 'O'
        else:
            currPlayerPiece = 'X'

        if i == 0:
            currPlayerPiece = 'X'
        
        # Print board
        board.printBoard(playerOne, playerTwo, initBoard)

        # Query for next player's placement
        if currPlayerPiece == 'X':
            print('\n' + playerOne + '\'s turn.')
        else:
            print('\n' + playerTwo + '\'s turn.')
        col, row = map(int, input('What is the row and column #\'s? EX- \'1 2\' : ').split())
        placement[0] = col
        placement[1] = row

        # Check valid placement and place into board.
        if board.isValidPlacement(placement, initBoard):
            initBoard[col][row] = currPlayerPiece
        else:
            print('\nERROR: Invalid choice. Please choose again.')

            # Flip player designation so it flips back accordingly.
            if currPlayerPiece == 'X':
                currPlayerPiece = 'O'
            else:
                currPlayerPiece = 'X'

            continue

        i += 1


    # Print board and claim victor.
    board.printBoard(playerOne, playerTwo, initBoard)
    if currPlayerPiece == 'X':
        print('\n' + playerOne + ' has won the game!')
    else:
        print('\n' + playerTwo + ' has won the game!')

    print("\nEnding the game now. Please restart the program if you want to play again.")

    return
    

# Menu Screen
print("Welcome to Tic Tac Toe built in Python!\n")
option = input('Type "start" when you are ready to begin! Otherwise, type "quit" if you want to exit the program. ')

if option == "start" or option == "Start":
    startGame()

elif option == "quit" or option == "Quit":
    print("Quitting the program....")
    quit
else:
    print("Invalid answer. Quitting the program.")
    quit

