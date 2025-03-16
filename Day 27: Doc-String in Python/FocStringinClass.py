class Dog:
    """
    A class representing a Dog.
    """
    def __init__(self, name):
        self.name = name
    
    def bark(self):
        """
        Makes the dog bark.
        """

        print(f"{self.name} says Woof!")

print(Dog.__doc__)
print(Dog.bark.__doc__)