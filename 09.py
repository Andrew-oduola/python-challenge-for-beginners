"""
9. Palindrome
Challenge: Define a function is_palindrome(x) that recognizes palindromes.
Explanation: This challenge requires you to check if a word reads the same backward as forward. 
It combines string manipulation and comparison.
"""


def reverse(x):
    new = []
    for i in range(len(x))[::-1]:
        new.append(x[i])
    # print(f'{new}')
    return ''.join(new)

print('radar'[::-1])

def is_palindrome(s):
    # if reverse(s) == s:
    if s[::-1] == s:
        print(f'{s}  is a palindrome')
    else:
        print(f'{s}  is not a palindrome')


is_palindrome('andrew')
is_palindrome('radar')
# print()
