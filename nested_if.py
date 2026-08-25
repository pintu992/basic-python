# nested if means if statement inside another if statement. It is used to check multiple conditions in a program. The inner if statement will only be executed if the outer if statement evaluates to true.
if True:
    print("Outer if statement is true")
    if True:
        print("Inner if statement is true")
    else:
        print("Inner if statement is false")
else:
    print("Outer if statement is false")