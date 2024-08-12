def modulus(a, b):
    if b == 0:
        return "Error: Division by zero is undefined"
    else:
        quotient = a // b
        product = quotient * b
        remainder = a - product
        return remainder



result = modulus(9.1, 0)
print(result)  

