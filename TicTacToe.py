def print_board(board):
    """Prints the current state of the Tic-Tac-Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * (len(row) * 3))

def check_win(board, player):
    """Checks if the given player has won."""
    size = len(board)
    # Rows, columns, and diagonals
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]]
    ]
    return any(all(cell == player for cell in condition) for condition in win_conditions)


def is_draw(board):
    """Checks if the game is a draw."""
    return all(all(cell != " " for cell in row) for row in board)

def get_valid_input(prompt, size):
    """Gets valid row or column input within the board range."""
    while True:
        try:
            value = int(input(prompt))
            if 0 <= value < size:
                return value
            print(f"Please enter a number between 0 and {size - 1}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def tic_tac_toe():
    """Main function to run the Tic-Tac-Toe game."""
    size = 3  # Default board size
    board = [[" " for _ in range(size)] for _ in range(size)]
    player = "X"

    while True:
        print_board(board)
        print(f"{player}'s turn.")
        
        row = get_valid_input("Enter the row: ", size)
        col = get_valid_input("Enter the column: ", size)

        if board[row][col] != " ":
            print("Invalid move! Cell already occupied. Try again.")
            continue

        board[row][col] = player

        if check_win(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            break

        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch player
        player = "O" if player == "X" else "X"

# Run the game
tic_tac_toe()

'''
Here's a line-by-line breakdown of the code:

Define print_board(board):
Prints the Tic-Tac-Toe board.
For each row, it joins the elements with " | " to format them as a row.
Separates rows with a line of dashes (---) for visual clarity.

Define check_win(board, player):
Checks if the given player has a winning condition.
Defines all possible winning combinations (rows, columns, and diagonals).
Uses a generator to check if any winning condition is met (all cells in a line match the player's symbol).

Define is_draw(board):
Checks if all cells on the board are occupied and no player has won.
Uses a nested loop to confirm that no cell contains a space (" ").

Define get_valid_input(prompt, size):
Prompts the player for valid input (row or column).
Ensures the input is an integer within the range of the board size (0 to size - 1).
Repeats the prompt until a valid input is provided.

Define tic_tac_toe():
Main function to manage the Tic-Tac-Toe game.

Set board size:
Creates a 3x3 board with all cells initialized to " " (empty).

Set initial player:
Player "X" goes first.

Game loop:
Repeatedly runs until there is a win or draw.

Print the current board:
Displays the current state of the game.

Prompt the current player:
Prints a message indicating whose turn it is (X or O).

Get user input for row and column:
Calls get_valid_input to ensure valid cell coordinates.

Check for an invalid move:
If the selected cell is already occupied, display an error and prompt the user to try again.

Mark the cell:
Updates the board with the player's symbol (X or O) at the chosen cell.

Check for a win:
Calls check_win to see if the current player has won.
If yes, displays the board and declares the winner. Ends the game.

Check for a draw:
Calls is_draw to see if the board is full with no winner.
If yes, displays the board and announces a draw. Ends the game.

Switch player:
Alternates between "X" and "O" after each turn.

Start the game:
The tic_tac_toe() function is called to run the game.
'''