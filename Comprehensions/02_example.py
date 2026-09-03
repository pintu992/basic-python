l = [lambda x: x*10 for x in range (1,5)]
print(l[0](1))  # Output: 10
print(l[1](2))  # Output: 20
for i in range(4):
    print(l[i](i+1))  # Output: 10, 20, 30, 40