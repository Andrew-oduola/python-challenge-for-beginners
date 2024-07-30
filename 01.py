"""
1. Max of Two Numbers
Challenge: Write a function max_of_two(a, b) that returns the maximum of two numbers.
Explanation: This is a basic problem where you need to compare two numbers and return the larger one. 
It introduces the concept of conditional statements in Python.
"""

def max_of_two(a, b):
    max = 0
    if a > b:
        max = a
    else:
        max = b

    print(f"The max of {a} and {b} is {max}")


max_of_two(1, 2)
max_of_two(12, 24)
max_of_two(51, 72)
max_of_two(13, 12)
max_of_two(109, 209)

