"""
4. Generate Character String
Challenge: Define a function generate_n_chars(n, c) that returns a string of length n consisting only of 
the character c.
Explanation: This problem helps you understand loops and string manipulation in Python. 
You’ll create a string by repeating a character n times.
"""

def generate_n_chars(n, c):
    lst = []
    for i in range(n):
        lst.append(c)

    text = ''.join(lst)
    print(text)


# print(5*'t')

generate_n_chars(4, 'r')
generate_n_chars(8, 'b')
generate_n_chars(3, 'a')
generate_n_chars(10, 'z')
