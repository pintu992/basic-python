# for loop
# for loop is used to iterate over a sequence (like a list, tuple, dictionary, set, or string) and execute a block of code for each item in the sequence.
for i in range(5):
    print(i)


# for loop with range function
"""range function is used to generate a sequence of numbers. It can take one, two, or three arguments.
If one argument is provided, it generates numbers from 0 to that number (exclusive). 
 If two arguments are provided, it generates numbers from the first argument to the second argument (exclusive). 
If three arguments are provided, it generates numbers from the first argument to the second argument (exclusive)
 with a step size of the third argument."""
n=int(input("Enter a number: "))
for i in range(1, 11):
    print(n*i)