def factorial(n):
    """
    Calculates the factorial of a non-negative integer.
    """
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

# Example usage:
number_to_calculate = 5
fact = factorial(number_to_calculate)
print(f"The factorial of {number_to_calculate} is: {fact}")
