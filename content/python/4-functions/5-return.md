# Return Statement

The `return` statement in Python is used to exit a function and optionally pass a value back to the caller. It is used to return the result of a function's execution.

---

```python
# Returning a value from a function
def add(a, b):
    return a + b

# Call the function and store the result
result = add(5, 3)
print(result)  # Output: 8

# Returning multiple values from a function
def get_coordinates():
    x = 10
    y = 20
    return x, y

# Call the function and unpack the returned tuple
x_coord, y_coord = get_coordinates()
print(x_coord, y_coord)  # Output: 10 20

# Returning nothing from a function
def greet(name):
    print(f"Hello, {name}!")
    return

# Call the function
greet("Alice")  # Output: Hello, Alice!
```