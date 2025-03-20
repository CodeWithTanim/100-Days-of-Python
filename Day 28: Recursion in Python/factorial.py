def factorial(n):
    if n == 1: #Base Case
        return 1
    else: #Recursive Steps
        return n * factorial(n-1)

print(factorial(5))