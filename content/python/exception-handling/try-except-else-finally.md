# Try Except Else Finally

The `else` block is executed if the code block inside the `try` block does not raise any exceptions. The `finally` block is executed after the `try` block and any `except` block.

```python
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print("Division successful:", result)
finally:
    print("End of try-except block.")

# Output: Division successful: 5.0
# Output: End of try-except block.
```