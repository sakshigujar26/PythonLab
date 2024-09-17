def str_to_int(text):
    """Convert a string of digits to an integer."""
    result = 0
    for char in text:
        digit = ord(char) - ord('0')
        result = result * 10 + digit
    return result

def subtract_digit_by_digit(a_str, b_str):
    """Subtract two numbers given as strings by manually handling borrowing."""
    # Convert strings to integers
    a = str_to_int(a_str)
    b = str_to_int(b_str)
    
    # Determine which number is larger to handle negative results
    if a < b:
        # Swap to ensure a is always greater than b for positive subtraction
        a, b = b, a
        is_negative = True
    else:
        is_negative = False
    
    # Convert to lists of digits (most significant digit first)
    a_digits = [int(d) for d in str(a)]
    b_digits = [int(d) for d in str(b)]
    
    # Ensure both lists have the same length by padding with zeros at the start
    max_len = max(len(a_digits), len(b_digits))
    a_digits = [0] * (max_len - len(a_digits)) + a_digits
    b_digits = [0] * (max_len - len(b_digits)) + b_digits
    
    result_digits = []
    borrow = 0
    
    # Subtract digit-by-digit with borrowing
    for i in range(max_len - 1, -1, -1):
        diff = a_digits[i] - b_digits[i] - borrow
        
        if diff < 0:
            diff += 10
            borrow = 1
        else:
            borrow = 0
        
        result_digits.append(diff)
    
    # Reverse the result digits back to normal order
    result_digits.reverse()
    
    # Convert result list of digits to an integer
    result_str = ''.join(map(str, result_digits)).lstrip('0') or '0'
    
    # Convert result to integer
    result = int(result_str)
    
    # Adjust the sign if needed
    if is_negative:
        result = -result
    
    return result

# Test cases
a_str = "1236"
b_str = "123"
result = subtract_digit_by_digit(a_str, b_str)
print(f"Original a: {a_str}")
print(f"Original b: {b_str}")
print(f"Result of subtraction: {result}")

# Additional test case
a_str = "19"
b_str = "123"
result = subtract_digit_by_digit(a_str, b_str)
print(f"Original a: {a_str}")
print(f"Original b: {b_str}")
print(f"Result of subtraction: {result}")

