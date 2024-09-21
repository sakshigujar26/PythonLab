def check_validity(text):
    
    brackets = {'(': ')', '{': '}', '[': ']', '<': '>'}
    stack = []
    
    for i, char in enumerate(text):
        # Ignore spaces
        if char == ' ':
            continue

        # Check if character is a valid opening bracket
        if char in brackets.keys():  # Opening bracket
            stack.append(char)
        
        # If it's a closing bracket
        elif char in brackets.values():  # Closing bracket
            
            if not stack:
                return f"Invalid: Closing bracket '{char}' at position {i} without opening bracket."
            elif char == brackets[stack[-1]]:
                stack.pop()  # Matched bracket, pop from stack
            else:
                return f"Invalid: Mismatched bracket '{stack[-1]}' and '{char}' at position {i}."
        else:
            # Invalid character
            return f"Invalid: Invalid character '{char}' at position {i}."

    # If stack is not empty a
    if stack:
        return f"Invalid: Unmatched opening bracket(s): {''.join(stack)}."

    return "Valid"


print(check_validity(" ) )"))  

