# Try Except Else

The `else` block is executed if the code block inside the `try` block does not raise any exceptions.

---

```python
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print("Division successful:", result)

# Output: Division successful: 5.0
```