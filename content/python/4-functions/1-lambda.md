# Lambdas

The lambda statement in Python is used to create small anonymous functions, also known as lambda functions. These functions can have any number of arguments but only one expression. They are often used for short, simple operations and can be defined in a single line.

---

```python
# Basic lambda function
# Define a lambda function to add two numbers
add = lambda a, b: a + b

# Call the lambda function
result = add(5, 3)
print(result)  # Output: 8

# Lambda function with no parameters
# Define a lambda function that takes no parameters
say_hello = lambda: "Hello, world!"

# Call the lambda function
print(say_hello())  # Output: Hello, world!

# Using lambda function inside another function
def apply_operation(x, y, operation):
    return operation(x, y)

# Call the function with a lambda function as an argument
result = apply_operation(5, 3, lambda a, b: a * b)
print(result)  # Output: 15

# Lambda function with a single parameter
# Define a lambda function to square a number
square = lambda x: x ** 2

# Call the lambda function
print(square(4))  # Output: 16
```