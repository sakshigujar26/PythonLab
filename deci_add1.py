def str_to_int(text):
    """Convert a string of digits to an integer."""
    result = 0
    for char in text:
        digit = ord(char) - ord('0')
        result = result * 10 + digit
    return result

def add_digit_by_digit(a_str, b_str):
    """Add two numbers given as strings by manually handling carrying."""
    # Convert strings to integers
    a = str_to_int(a_str)
    b = str_to_int(b_str)
    
    # Convert to lists of digits (most significant digit first)
    a_digits = [int(d) for d in str(a)]
    b_digits = [int(d) for d in str(b)]
    
    # Ensure both lists have the same length by padding with zeros at the start
    max_len = max(len(a_digits), len(b_digits))
    a_digits = [0] * (max_len - len(a_digits)) + a_digits
    b_digits = [0] * (max_len - len(b_digits)) + b_digits
    
    result_digits = []
    carry = 0
    
    # Add digit-by-digit with carrying
    for i in range(max_len - 1, -1, -1):
        total = a_digits[i] + b_digits[i] + carry
        
        if total >= 10:
            carry = 1
            total -= 10
        else:
            carry = 0
        
        result_digits.append(total)
    
    # If there's a carry left after the last addition, append it
    if carry:
        result_digits.append(carry)
    
    # Reverse the result digits back to normal order
    result_digits.reverse()
    
    # Convert result list of digits to an integer
    result_str = ''.join(map(str, result_digits)).lstrip('0') or '0'
    
    return int(result_str)

# Test cases
a_str = "1236"
b_str = "123"
result = add_digit_by_digit(a_str, b_str)
print(f"a: {a_str}")
print(f"b: {b_str}")
print(f"Result of addition: {result}")


