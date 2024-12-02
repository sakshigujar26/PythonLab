def is_leap_year(year):
    """Check if a year is a leap year."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def get_days_in_month(year, month):
    """Return the number of days in a given month of a specific year."""
    if month == 2:  # February
        return 29 if is_leap_year(year) else 28
    elif month in {4, 6, 9, 11}:  # April, June, September, November
        return 30
    else:
        return 31

def get_start_day_of_month(year, month):
    """Calculate the day of the week the month starts on (0=Monday, 6=Sunday)."""
    if month < 3:
        month += 12
        year -= 1
    q = 1  # Day of the month
    K = year % 100
    J = year // 100
    start_day = (q + ((13 * (month + 1)) // 5) + K + (K // 4) + (J // 4) - (2 * J)) % 7
    return (start_day + 5) % 7  # Convert to 0=Monday, 6=Sunday

def print_month(year, month):
    """Generate the calendar for a specific month."""
    # Month names
    month_names = ["January", "February", "March", "April", "May", "June",
                   "July", "August", "September", "October", "November", "December"]
    
    # Calculate the start day and number of days
    start_day = get_start_day_of_month(year, month)
    days_in_month = get_days_in_month(year, month)

    # Create header for the month
    result = [f"  {month_names[month - 1]} {year}".center(20)]
    result.append("Mo Tu We Th Fr Sa Su")

    # Create rows of days
    week = ["  "] * start_day  # Initialize the first row with empty spaces
    for day in range(1, days_in_month + 1):
        week.append(f"{day:2}")  # Add the day formatted with 2 spaces
        if len(week) == 7:
            result.append(" ".join(week))  # Print the full week
            week = []  # Reset the week

    if week:  # If there are remaining days in the last week
        result.append(" ".join(week).ljust(20))  # Print the last partial week

    return result

def print_calendar_grid(year, rows, cols):
    """Print the calendar in a grid of rows x cols."""
    total_months = 12
    months = [print_month(year, month) for month in range(1, total_months + 1)]

    if rows * cols < total_months:
        print("Error: The grid dimensions must accommodate all 12 months.")
        return

    # Print the calendar grid
    for row in range(rows):
        for line in range(8):  # Each month has up to 8 lines
            for col in range(cols):
                month_index = row * cols + col
                if month_index < total_months:
                    month_data = months[month_index]
                    if line < len(month_data):
                        # Ensure proper alignment with fixed-width columns
                        print(month_data[line].ljust(20), end="  ")
                    else:
                        print(" " * 20, end="  ")  # Blank space for missing rows
                else:
                    print(" " * 20, end="  ")  # Fill blank spaces for grid alignment
            print()
        print()  # Separate rows of the grid

# Input year and grid dimensions
year = int(input("Enter year (e.g., 2024): "))
rows, cols = map(int, input("Enter rows and columns for calendar grid (e.g., 3 4): ").split())

# Print the calendar grid
print_calendar_grid(year, rows, cols)

