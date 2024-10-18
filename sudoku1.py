import random

# Function to print the 9x9 Sudoku grid with proper borders
def print_sudoku_grid(grid):
    for i in range(9):
        if i % 3 == 0:  # Print a horizontal separator every 3 rows
            print("-" * 25)
        row = ""
        for j in range(9):
            if j % 3 == 0:  # Print a vertical separator every 3 columns
                row += "| "
            row += str(grid[i][j]) if grid[i][j] != 0 else " "  # Empty cells are shown as spaces
            row += " "
        row += "|"
        print(row)
    print("-" * 25)  # Final horizontal separator at the bottom

# Check if the current move is valid (no conflicts in row, column, and 3x3 sub-grid)
def is_valid_move(grid, row, col, num):
    # Check row
    if num in grid[row]:
        return False
    # Check column
    if num in [grid[i][col] for i in range(9)]:
        return False
    # Check 3x3 sub-grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if grid[i][j] == num:
                return False
    return True

# Generate a 9x9 Sudoku grid with some cells filled based on difficulty level
def generate_partial_sudoku_grid(level):
    grid = [[0 for _ in range(9)] for _ in range(9)]  # Start with an empty grid

    # Fill 30 cells for easy, 20 cells for medium, 10 cells for hard
    num_filled = 30 if level == 'easy' else 20 if level == 'medium' else 10

    for _ in range(num_filled):
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        num = random.randint(1, 9)
        if grid[row][col] == 0 and is_valid_move(grid, row, col, num):
            grid[row][col] = num
    return grid

# Check if the Sudoku is solved (no empty cells)
def is_sudoku_solved(grid):
    for row in grid:
        if 0 in row:
            return False
    return True

# Function to play the Sudoku game
def play_sudoku():
    # Ask user for the difficulty level
    while True:
        level = input("Choose difficulty level (easy, medium, hard): ").lower()
        if level in ['easy', 'medium', 'hard']:
            break
        else:
            print("Invalid choice! Please select from easy, medium, or hard.")
    
    grid = generate_partial_sudoku_grid(level)  # Generate initial grid based on level
    while not is_sudoku_solved(grid):
        print_sudoku_grid(grid)  # Display the current grid
        try:
            # Get user input for row, column, and number
            row, col, num = map(int, input("Enter row (0-8), column (0-8), and number (1-9), separated by spaces: ").split())
            if 0 <= row < 9 and 0 <= col < 9 and 1 <= num <= 9:
                if grid[row][col] == 0 and is_valid_move(grid, row, col, num):
                    grid[row][col] = num  # Place the number in the grid
                else:
                    print("Invalid move! Either the cell is filled or the number conflicts with row, column, or sub-grid.")
            else:
                print("Invalid input! Please enter values within the valid range.")
        except ValueError:
            print("Invalid input! Please enter three integers.")
    
    print("Congratulations! You solved the Sudoku puzzle!")
    print_sudoku_grid(grid)  # Display the solved grid

# Start the game
play_sudoku()

