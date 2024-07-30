"""
5. Max of Three Numbers
Challenge: Write a function max_of_three(a, b, c) that returns the maximum of three numbers.
Explanation: This challenge extends the concept of finding the maximum to three numbers. 
It’s an introduction to more complex conditional logic.
"""


def max_of_three(a, b, c):
    max = 0
    if a > b and a > c:
        max = a
    elif b > a and b > c:
        max = b
    else:
        max = c

    print(f"The max of {a}, {b}, {c} is {max}")

# print(max(1, 2, 33, 5, 6))

max_of_three(1, 2, 3)
max_of_three(5, 2, 3)
max_of_three(1, 8, 3)
max_of_three(12, 2, 3)
