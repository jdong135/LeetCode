# Binary to decimal
def binaryToDecimal(val):
    val = str(val)
    num = 0
    for digit in val:
        num = 2 * num + int(digit)
    return num

def binaryToDecimal2(val):
    val = str(val)
    num = 0
    for digit in val:
        num = (num << 1) | int(digit)
    return num

# Decimal to binary
def decimalToBinary(val):
    binary = ""
    while val != 0:
        binary = str(val % 2) + binary
        val = val // 2
    return int(binary)

# Decimal to any base < 10:
def decimalToBase(val, base):
    output = ""
    while val != 0:
        output = str(val % base) + output
        val = val // base
    return int(output)

# Decimal to any base < 10 recursive:
def decimalToBase2(val, base):
    if val > base - 1:
        decimalToBase2(val // base, base)
    print(val % base)

# Decimal to base between (10, 16]:
def decimalToBase(val, base):
    letters = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    output = ""
    while val != 0:
        remainder = val % base
        if remainder > 9:
            remainder = letters[val % base]
        output = str(remainder) + output
        val = val // base
    return output
