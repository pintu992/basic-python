class dog():
    species = "rural"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says Woof!"

d1 = dog("Buddy", 3)
print(d1.bark())  # Output: Buddy says Woof!
print(d1.species)  # Output: rural