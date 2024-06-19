# Try Except Finally

The `finally` block is executed after the `try` block and any `except` block.

```python
try:
    file = open("example.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found!")
finally:
    if 'file' in locals() and not file.closed:
        file.close()
    print("File operation complete.")

# Output (if file does not exist): File not found!
# Output (always): File operation complete.
```