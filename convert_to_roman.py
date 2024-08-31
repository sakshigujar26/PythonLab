def to_roman(n, number_system):
    def decimal_to_system(n, number_system):
        # Convert the decimal number to the specified number system
        if number_system == "binary":
            return bin(n)[2:]  
        elif number_system == "hexadecimal":
            return hex(n)[2:]  
        elif number_system == "octal":
            return oct(n)[2:]  
        else:
            raise ValueError("Unsupported number system")
    
    def system_to_decimal(system_value, number_system):
        # Convert a number in the specified system to decimal
        if number_system == "binary":
            return int(system_value, 2)
        elif number_system == "hexadecimal":
            return int(system_value, 16)
        elif number_system == "octal":
            return int(system_value, 8)
        else:
            raise ValueError("Unsupported number system")
    
    def convert_to_roman(decimal_number):
        # Roman numeral mapping
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        
        roman_num = ''
        i = 0
        while decimal_number > 0:
            for _ in range(decimal_number // val[i]):
                roman_num += syb[i]
                decimal_number -= val[i]
            i += 1
        return roman_num
    
    
    system_value = decimal_to_system(n, number_system)
    
    
    decimal_value = system_to_decimal(system_value, number_system)
    
    
    if decimal_value < 1 or decimal_value > 3999:
        return "Roman numerals can only represent numbers from 1 to 3999."
    
   
    return convert_to_roman(decimal_value)


print(to_roman(10, "binary"))       

