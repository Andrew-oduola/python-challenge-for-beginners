"""
12. Convert Binary to Decimal
Challenge: Write a function binary_to_decimal(binary) that converts a binary number (given as an integer) to its decimal equivalent.
Explanation: This problem involves converting a binary number to its decimal form. 
It demonstrates the use of loops and mathematical operations.
"""

def binary_to_decimal(binary):
    decimal, i = 0, 0 
    while (binary != 0):
        dec = binary % 10 
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1

    return f"Decimal is {decimal}"

print(binary_to_decimal(1))
print(binary_to_decimal(10))
print(binary_to_decimal(11))
print(binary_to_decimal(100))
print(binary_to_decimal(101))
print(binary_to_decimal(110))
print(binary_to_decimal(111))
print(binary_to_decimal(1000))
print(binary_to_decimal(1000001))
print(binary_to_decimal(1011111))

        
