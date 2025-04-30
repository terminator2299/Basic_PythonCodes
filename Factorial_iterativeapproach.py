def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Example usage
num = int(input("Enter a number: "))
print("Factorial:", factorial(num))