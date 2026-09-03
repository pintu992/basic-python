try:
    a=2
    b=0
    c=a/b
except ZeroDivisionError as e:
    print("Error: ", e)