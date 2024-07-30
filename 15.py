"""
15. Fibonacci Sequence
Challenge: Write a function fibonacci(n) that returns the first n numbers in the Fibonacci sequence.
Explanation: This challenge requires generating a sequence where each number is the sum of the two preceding ones. 
It’s a classic problem that demonstrates recursion or iterative approaches.
"""

# [0, 1, 1, 2]

def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        
    print(fib_sequence[:n])


fibonacci(10)
# fibonacci(100)
fibonacci(13)
fibonacci(5)
# fibonacci(78)

