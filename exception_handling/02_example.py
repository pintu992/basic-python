try:
    while True:
        a = int(input("Enter a number: "))
        b = int(input("Enter another number: "))
        c = a / b
        print("Result: ", c)
except ValueError:
    print("Please enter valid integers.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")