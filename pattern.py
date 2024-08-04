def pattern(n):
    
    if n <= 0:
        print("Enter a length of 1 or greater to see the pattern")
        return

    middle = n  # The middle index where the integer should be placed

    # Calculate the width of the widest part of the pattern
    max_width = 2 * n + 1

    # Top half of the diamond
    for i in range(n):
        # Print leading spaces
        for j in range(n - i):
            print(" ", end=" ")

        # Print pattern characters
        for k in range(2 * i + 1):
            if k == 0 or k == 2 * i:
                # Print border
                print("*", end=" ")
            elif i == middle and k == middle:
                # Print the integer in the exact center
                print(n, end=" ")
            else:
                print(" ", end=" ")

        print()

    # Bottom half of the diamond
    for i in range(n, -1, -1):
        # Print leading spaces
        for j in range(n - i):
            print(" ", end=" ")

        # Print pattern characters
        for k in range(2 * i + 1):
            if k == 0 or k == 2 * i:
                # Print border
                print("*", end=" ")
            elif i == middle and k == middle:
                # Print the integer in the exact center
                print(n, end=" ")
            else:
                print(" ", end=" ")

        print()

    # Additional lines at the bottom
    bottom_line_count = n
    stars_count = 2 * n + 3  # Number of stars in each bottom line

    # Print bottom lines
    for _ in range(bottom_line_count):
        leading_spaces = (max_width - stars_count) // 2
        print(" " * leading_spaces + "* " * stars_count)

# Get user input and call the function
length = int(input("Enter the length: "))
pattern(length)

