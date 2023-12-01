def factorial(n):
    result = n
    for i in range(n - 1, 0, -1):
        result *= i
    return result

print(factorial(4))