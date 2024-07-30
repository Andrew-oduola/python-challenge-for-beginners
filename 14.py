"""
14. Longest Word in a List
Challenge: Write a function find_longest_word(words) that returns the length of the longest word in a list of words.
Explanation: This problem involves finding the longest word in a list. 
It requires iterating through the list and comparing the lengths of each word.
"""

def find_longest_word(words):
    max_word = 0
    for i in words:
        if len(i) > max_word:
            max_word = len(i)

    print(max_word)


find_longest_word(['apple', 'orange', 'mango'])
find_longest_word(['Mosh', 'Andrew', 'Tim'])
find_longest_word(['Paul', 'Max', 'Math'])
find_longest_word(['Male', 'Female', 'Girl'])
find_longest_word(['Boy', 'Man', 'Woman'])

