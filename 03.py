"""
3. Check if a Letter is a Vowel
Challenge: Write a function is_vowel(c) that checks if a given character is a vowel.
Explanation: This challenge requires you to check if a character is one of the vowels (a, e, i, o, u). 
It demonstrates the use of conditionals and string operations.
"""

def is_vowel(c):
    vowel_letters = 'aeiou'
    if c.lower() in vowel_letters:
        print(f" '{c}' is a vowel letter")
    else:
        print(f" '{c}' is not a vowel")


is_vowel('A')
is_vowel('c')
is_vowel('a')
is_vowel('b')
is_vowel('r')
is_vowel('i')
is_vowel('l')
