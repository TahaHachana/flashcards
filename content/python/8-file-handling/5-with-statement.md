# With Statement

The `with` statement in Python is used to simplify exception handling by encapsulating common preparation and cleanup tasks in so-called context managers. The `with` statement is used to wrap the execution of a block of code within methods defined by a context manager.

The `with` statement is commonly used to open files, acquire locks, and more. When the block of code is exited, the context manager's `__exit__()` method is called to clean up resources.

```python
# Open a file using the with statement
with open("example.txt", "r") as file:
    # Read the entire content of the file
    content = file.read()
    print(content)
# No need to explicitly close the file; it's done automatically
```