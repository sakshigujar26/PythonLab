def is_valid_bracket_sequence(text):
    stack = []
    bracket_map = {')': '(', ']': '[', '}': '{'}
    
    for char in text:
        if char in bracket_map.values():  # If it's an opening bracket
            stack.append(char)
        elif char in bracket_map.keys():  # If it's a closing bracket
            if stack == [] or bracket_map[char] != stack.pop():
                return False
    return stack == []  # Stack should be empty if valid

def get_valid_invalid_text_count(texts):
    valid_count = 0
    invalid_count = 0
    
    for text in texts:
        if isinstance(text, str):  # Check if the object is a string
            if is_valid_bracket_sequence(text):
                valid_count += 1
            else:
                invalid_count += 1
                
    return (valid_count, invalid_count)



result = get_valid_invalid_text_count(['[{(', [45], "((", ']'])
print(result)  # Correct Output: (1, 2)

