# Using %-formatting

This is an older method of formatting strings in Python. It uses the `%` operator to format a set of variables enclosed in a tuple (fixed-size array). The format string contains one or more format codes, which specify how the values should be formatted.

---

```python
name = "Alice"
age = 30
print("My name is %s and I am %d years old." % (name, age))
# Output: My name is Alice and I am 30 years old.
```