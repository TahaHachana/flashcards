# Basic try-except

The try statement in Python is used to handle exceptions, allowing you to catch and respond to errors that occur during the execution of a program. It works with except, else, and finally blocks to provide a robust error-handling mechanism.

---

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Output: Cannot divide by zero!
```