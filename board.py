# Board manipulation module.


# Builds/Initializes an empty board.
def buildBoard():

    # Initialize the board.
    board = [['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', '']]

    # Send the board back to the driver program.
    return board


# Prints the current state of the board.
def printBoard(playerOne, playerTwo, currBoard):

    # Set the title that will display over the board.
    title = 'Player 1 = ' + playerOne + '\tPlayer 2 = ' + playerTwo + '\nX\tO'

    print(title)

    # Go through the current board and print it out.
    for i in range(len(currBoard)):
        for j in range(len(currBoard[j])):
            
            if j == 2:
                print('| ' + currBoard[i][j] + ' |')
            else:
                print('| ' + currBoard[i][j] + ' ')

    print()

    return


# Function to check the state of the board for any wins/draws.
def stateCheck(currBoard, currPlayerPiece):

    col = 0
    row = 0

    # Check for different potential victories.

    # Check for NW -> SE victory.
    if currBoard[col][row] == currPlayerPiece:
        if currBoard[col + 1][row + 1] == currPlayerPiece:
            if currBoard[col + 2][row + 2] == currPlayerPiece:
                return True
    
    # Check for NE -> SW victory.
    elif currBoard[col + 2][row] == currPlayerPiece:
        if currBoard[col + 1][row + 1] == currPlayerPiece:
            if currBoard[col][row + 2] == currPlayerPiece:
                return True

    # Check for first row victory.
    elif currBoard[col + 1][row] == currPlayerPiece:

        # Final check for first row victory.
        if currBoard[col + 2][row] == currPlayerPiece:
            return True
        
        # Check for second column victory.
        elif currBoard[col + 1][row + 1] == currPlayerPiece:

            # Final check for second column victory.
            if currBoard[col + 1][row + 2] == currPlayerPiece:
                return True
    
    # Check for first column victory.
    elif currBoard[col][row + 1] == currPlayerPiece:

        # Final check for first column victory.
        if currBoard[col][row + 2] == currPlayerPiece:
            return True

        # Check for second row victory.
        elif currBoard[col + 1][row + 1] == currPlayerPiece:
            
            # Final check for second row victory.
            if currBoard[col + 2][row + 1]:
                return True
        
    # Check for last row victory.
    elif currBoard[col][row + 2] == currPlayerPiece:
        if currBoard[col + 1][row + 2] == currPlayerPiece:
            if currBoard[col + 2][row + 2] == currPlayerPiece:
                return True

    # Check for last column victory.
    elif currBoard[col + 2][row] == currPlayerPiece:
        if currBoard[col + 2][row + 1] == currPlayerPiece:
            if currBoard[col + 2][row + 2] == currPlayerPiece:
                return True

    return False


# Function to check if the chosen location is a valid choice or not.
def isValidPlacement(placement, currBoard):

    # Store index.
    col = placement[0]
    row = placement[1]

    # If not empty, then it is not a valid placement.
    if currBoard[col][row] != "":
        return False

    return True
