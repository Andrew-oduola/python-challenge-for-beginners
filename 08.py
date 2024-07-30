"""
8. Reverse a String
Challenge: Define a function reverse(x) that computes the reversal of a string.
Explanation: This problem involves reversing a string. 
It demonstrates the use of slicing in Python, which is a powerful feature for string manipulation.
"""

def reverse(x):
    new = []
    for i in range(len(x))[::-1]:
        new.append(x[i])
    print(f'{new}')
    print(''.join(new))

reverse('andrew')
reverse('I am coding')
reverse('I am cooking')
reverse('Run run run')