"""
11. Count Vowels in a String
Challenge: Write a function count_vowels(s) that counts the number of vowels in a given string.
Explanation: This challenge requires counting the number of vowels in a string. 
It involves iterating through the string and checking each character.
"""

def count_vowels(s):
    vowel = 'aeiou'
    count = 0
    for i in s:
        if i.lower() in vowel:
            count += 1


    return f"There are {count} vowels in {s}"

print(count_vowels('Andrew'))
print(count_vowels('Drex'))
print(count_vowels('Paul'))
print(count_vowels('Boy'))
print(count_vowels('bread'))

