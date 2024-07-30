"""
13. Maximum in a List
Challenge: Write a function max_in_list(lst) that returns the largest number in a list.
Explanation: This challenge requires finding the maximum number in a list. 
It’s an extension of the max function to handle lists of any size.
"""

def max_in_list(lst):
    max = 0
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1] and lst[i] > max:
            max = lst[i]
        elif lst[i+1] > max:
            max = lst[i+1]

    print(max)


max_in_list([1, 2, 3, 5, 6, 3, 63])
max_in_list([1, 2, 3, 53, 6, 3, 6])
max_in_list([1, 23, 3, 5, 6, 3])
max_in_list([1, 2, 12, 5, 6])