def decimal_to_base(num, base):
    digits = "0123456789abcdefghijklmnopqrstuvwxyz"
    if num == 0:
        return "0"

    result = ""
    while num > 0:
        result = digits[num % base] + result
        num //= base

    return result

def get_base_value(base_str):
    if base_str.isdigit():
        return int(base_str)
    elif base_str.isalpha() and len(base_str) == 1:
        base_str = base_str.lower()
    if 'a' <= base_str <= 'z':
        return ord(base_str) - ord('a') + 11
    else:
        return 0

def base(text, input_base, output_base):
    num = base_to_decimal(text, input_base)
    
    if output_base == 'r':
        return roman(num)  # Pass the decimal number to the roman() function
    elif output_base == '10':
        return str(num)
    else:
        base = get_base_value(output_base)
        if 2 <= base <= 36:
            return decimal_to_base(num, base)
        else:
            return "Invalid base"

def base_to_decimal(num_str, base):
    digits = "0123456789abcdefghijklmnopqrstuvwxyz"
    num = 0
    power = 0  # Start with the least significant digit
    
    for char in reversed(num_str):
        value = digits.index(char.lower())
        num += value * (base ** power)
        power += 1  # Increment the power for the next digit

    return num

def roman(num):
    roman_dict = {
        1000: 'M', 
        900: 'CM', 
        500: 'D', 
        400: 'CD', 
        100: 'C',
        90: 'XC', 
        50: 'L', 
        40: 'XL', 
        10: 'X', 
        9 : 'IX', 
        5 : 'V', 
        4 : 'IV', 
        1 : 'I'
    }

    int_roman = sorted(roman_dict.keys(), reverse=True)
    roman_numeral = ""
    
    
    for i in int_roman:
        while num >= i:
            roman_numeral += roman_dict[i]
            num -= i
            
    return roman_numeral

# Example of calling the base conversion
result = print(base('26', 10, 'r')) 

