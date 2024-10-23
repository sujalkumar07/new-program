# : Write a Python function factorial(n) that calculates and returns the factorial of a number n using recursion.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)
    
result = factorial(5)
print(result)