# Init

The __init__ method in Python is a special method called a constructor. It is automatically called when a new instance of a class is created. The __init__ method initializes the instance's attributes.

```python
class Dog:
    """
    A simple class representing a dog.
    """

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def bark(self):
        return f"{self.name} is barking!"

    # Instance method
    def get_age(self):
        return f"{self.name} is {self.age} years old."

# Create an instance of the Dog class
my_dog = Dog("Buddy", 3)

# Access instance attributes
print(my_dog.name)  # Output: Buddy
print(my_dog.age)   # Output: 3

# Call instance methods
print(my_dog.bark())  # Output: Buddy is barking!
print(my_dog.get_age())  # Output: Buddy is 3 years old.
```