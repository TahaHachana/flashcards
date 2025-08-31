# Try-except with Multiple Exceptions

---

```python
try:
    result = int("abc")
except ValueError:
    print("Invalid input! Cannot convert to integer.")
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Output: Invalid input! Cannot convert to integer.
```