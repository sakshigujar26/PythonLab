def binary_subtraction(bin1, bin2):
    # Ensure both binary numbers have the same length by padding with leading zeros
    max_len = max(len(bin1), len(bin2))
    bin1 = bin1.zfill(max_len)
    bin2 = bin2.zfill(max_len)

    result = ''
    carry = 0

    # Perform subtraction bit by bit from right to left
    for i in range(max_len - 1, -1, -1):
        bit1 = int(bin1[i])
        bit2 = int(bin2[i])

        # Subtract the bits and account for carry
        sub = (bit1 - bit2 - carry)

        if sub == 0:
            result = '0' + result
            carry = 0
        elif sub == 1:
            result = '1' + result
            carry = 0
        elif sub == -1:
            result = '1' + result
            carry = 1
        elif sub == -2:
            result = '0' + result
            carry = 1

    # Remove leading zeros from the result
    result = result.lstrip('0')

    # If the result is empty, the result is 0
    if not result:
        return '0'
    return result

# Example usage
bin1 = "1100"  # Binary for 12
bin2 = "1000"  # Binary for 8

result = binary_subtraction(bin1, bin2)
print(f"Binary subtraction of {bin1} - {bin2} = {result}")

