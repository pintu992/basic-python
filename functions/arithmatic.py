""" function is a block of code that is used to perform a specific task.
It can take input in the form of parameters and can return output in the form of return values. 
Functions are used to break down a program into smaller, manageable parts and to avoid code repetition."""

def addition(a, b):
    """This function takes two parameters a and b and returns their sum."""
    return a + b

def subtraction(a, b):
    """This function takes two parameters a and b and returns their difference."""
    return a - b

def multiplication(a, b):
    """This function takes two parameters a and b and returns their product."""
    return a * b

def division(a, b):
    """This function takes two parameters a and b and returns their quotient."""
    return a / b 

# function calling
addition_result = addition(10, 5)
subtraction_result = subtraction(10, 5)
multiplication_result = multiplication(10, 5)
division_result = division(10, 5)
print("Addition: ", addition_result)
print("Subtraction: ", subtraction_result)
print("Multiplication: ", multiplication_result)
print("Division: ", division_result)