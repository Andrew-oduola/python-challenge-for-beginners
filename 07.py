"""
7. Check if a List is Sorted
Challenge: Write a function is_sorted(lst) that checks if a list is sorted in either ascending or descending order.
Explanation: This challenge requires you to check the order of elements in a list. 
It involves iterating through the list and comparing adjacent elements to determine if the list is sorted.
"""

list_1 = [1, 2, 3, 4]

def is_sorted(lst):
    asc, desc = True, True
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            asc = False

    for i in range(len(lst)-1):
        if lst[i] < lst[i+1]:
            desc = False

    if asc or desc:
        print(f'{lst}  is sorted')
    else:
        print(f'{lst}  is  not sorted')


list_1 = [1, 2, 3, 4]
list_2 = [1, 22, 3, 4]
list_3 = [4, 3, 2, 1]
list_4 = [1, 2, 33, 4]
list_5 = [1, 2, 3, 4]
list_6 = [11, 2, 3, 4]

is_sorted(list_1)
is_sorted(list_2)
is_sorted(list_3)
is_sorted(list_4)
is_sorted(list_5)
is_sorted(list_6)

