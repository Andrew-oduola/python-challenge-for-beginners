"""
6. Sum and Multiplication of Numbers in a List
Challenge: Write a function sum_and_multiplication(lst) that returns the sum and multiplication of all the numbers in a list.
Explanation: This problem involves iterating through a list to calculate both the sum and the product of its elements. 
It demonstrates the use of loops and basic arithmetic operations.
"""


def sum_list(lst):
    sum = 0
    for i in lst:
        sum += i

    print(sum)

def mul_list(lst):
    mul = 1
    for i in lst:
        mul *= i

    print(mul)

list_1 = [1, 2, 3]
list_2 = [1, 2, 3, 5, 6 ,7]
list_3 = [1, 2, 33, 23, 53]
list_4 = [123, 23, 3]
list_5 = [122, 2233, 23]

# print(sum(list_2))

# sum_list(list_1)
# sum_list(list_2)
# sum_list(list_3)
# sum_list(list_4)
# sum_list(list_5)

mul_list(list_1)
mul_list(list_2)
mul_list(list_3)
mul_list(list_4)
mul_list(list_5)