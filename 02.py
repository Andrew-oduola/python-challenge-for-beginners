"""
2. Length of a String
Challenge: Write a function string_length(s) that returns the length of a given string.
Explanation: This problem involves finding the length of a string using Python's built-in len() function. 
It’s a simple exercise to understand how to work with strings.
"""

def string_length(s):
    count = 0
    for i in s:
        count += 1

    print(f"The length of '{s}' is {count}")

string_length('Andrew')
string_length('Drex')
string_length('I love coding')
string_length('I am going to the market')
string_length('Mummy is cooking')
string_length('My dad is reading the newspaper')