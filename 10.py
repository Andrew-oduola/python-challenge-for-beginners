"""
10. Words Longer than N in a List
Challenge: Write a function filter_long_words(words, n) that returns the list of words longer than n.
Explanation: This problem involves filtering word lists based on length. 
It demonstrates list comprehension, a concise way to create lists in Python.
"""

def filter_long_words(words, n):
    lst = []
    for i in words:
        if len(i) > n:
            lst.append(i)
        
    print(lst)


fruits = ['apple', 'banana', 'mango', 'pineapple']
filter_long_words(fruits, 9)