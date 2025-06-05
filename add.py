def add_numbers(a, b):
    """
    This function takes two numbers as input and returns their sum.
    """
    return a + b

# Example usage
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

result = add_numbers(num1, num2)
print(f"The sum of {num1} and {num2} is {result}.")