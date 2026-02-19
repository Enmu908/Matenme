# Basic Complexity Exercises

# Exercise 1: Fibonacci Sequence

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Exercise 2: Factorial

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Exercise 3: Prime Check

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Exercise 4: Sorting

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Usage Examples:
# print(list(fibonacci(10)))
# print(factorial(5))
# print(is_prime(11))
# print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))