# Python Tic-Tac-Toe

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
option = input('Type "start" when you are ready to begin! Otherwise, type "quit" if you want to exit the program.\n')

if option == "start" or option == "Start":
    startGame()

elif option == "quit" or option == "Quit":
    print("Quitting the program....")
    quit
else:
    print("Invalid answer. Quitting the program.")
    quit

