import random

def game():
    # Get grid dimensions from the user
    while True:
        try:
            x = int(input("Enter number of columns: "))
            y = int(input("Enter number of rows: "))
            if x > 0 and y > 0:
                break
            else:
                print("Please enter positive integers for rows and columns.")
        except ValueError:
            print("Invalid input! Please enter integers.")

    # Initialize the grid as a dictionary with keys as (row, col) tuples and values as empty strings
    grid = {(row, col): " " for row in range(y) for col in range(x)}

    def print_grid():
        # Create the horizontal component (top and bottom border of each row)
        horizontal = " ---" * x  # Horizontal line for each column
        for row in range(y):
            # Print the top border of the current row
            print(horizontal)
            # Create and print the cells of the current row with vertical separators
            row_data = "| " + " | ".join(grid[(row, col)] for col in range(x)) + " |"
            print(row_data)
        # Print the bottom border after the last row
        print(horizontal)

    def check_winner(player):
        # Check rows
        for row in range(y):
            if all(grid[(row, col)] == player for col in range(x)):
                return True

        # Check columns
        for col in range(x):
            if all(grid[(row, col)] == player for row in range(y)):
                return True

        # Check diagonals (only valid if the grid is square)
        if x == y:
            # Check main diagonal (top-left to bottom-right)
            if all(grid[(i, i)] == player for i in range(x)):
                return True
            # Check anti-diagonal (top-right to bottom-left)
            if all(grid[(i, x - 1 - i)] == player for i in range(x)):
                return True

        return False

    # Randomly decide who starts first
    current_player = random.choice(["player1", "player2"])  # Could be Player 1 or Player 2 (X or O)
    print(f"Randomly selected: Player {current_player} will start!")

    for turn in range(x * y):
        print_grid()  # Show the updated grid
        print(f"Player {current_player}, enter your move (row and column): ")

        # Loop until a valid move is entered
        while True:
            try:
                # Get row and column input
                row, col = map(int, input("Enter row and column numbers (0-indexed): ").split())

                # Check if the input is within grid bounds
                if 0 <= row < y and 0 <= col < x:
                    # Check if the cell is empty
                    if grid[(row, col)] == " ":
                        grid[(row, col)] = current_player  # Make the move
                        break
                    else:
                        print("Cell is already taken! Choose another.")
                else:
                    print(f"Invalid move! Row should be between 0 and {y-1}, and column between 0 and {x-1}.")
            except (ValueError, IndexError):
                print("Invalid input! Please enter row and column numbers (e.g., 0 0).")

        # Check if the current player has won
        if check_winner(current_player):
            print_grid()  # Show the final grid
            print(f"Player {current_player} wins!")
            return  # End the game

        # Switch players after each valid move
        current_player = "O" if current_player == "X" else "X"

    print_grid()  # Show the final grid
    print("It's a draw!")

# Start the game
game()

