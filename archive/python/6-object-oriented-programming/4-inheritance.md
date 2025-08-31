# Inheritance

Inheritance in Python is a mechanism that allows a class (called the child or subclass) to inherit attributes and methods from another class (called the parent or superclass). This promotes code reuse and can create a hierarchical relationship between classes.

---

```python
# Define the parent class
class Animal:
    """
    A simple class representing an animal.
    """

    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

# Define the child class
class Dog(Animal):
    """
    A class representing a dog, inheriting from Animal.
    """

    def __init__(self, name, age):
        # Call the constructor of the parent class
        super().__init__(name)
        self.age = age

    def speak(self):
        return f"{self.name} says Woof!"

# Create an instance of the Dog class
my_dog = Dog("Buddy", 3)

# Access attributes and methods
print(my_dog.name)  # Output: Buddy
print(my_dog.age)   # Output: 3
print(my_dog.speak())  # Output: Buddy says Woof!
```