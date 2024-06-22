# Class Keyword

The `class` keyword in Python is used to define a class, which is a blueprint for creating objects. A class encapsulates data and functionality together.

---

```python
class Dog:
    """
    A simple class representing a dog.
    """

    # Class attribute
    species = "Canis familiaris"

    # Instance method
    def bark(self):
        return "Woof!"

# Create an instance of the Dog class
my_dog = Dog()

# Access class attribute
print(my_dog.species)  # Output: Canis familiaris

# Call instance method
print(my_dog.bark())  # Output: Woof!
```