# File Parameter

The `file` parameter in the `print()` function is used to specify the file to write the output to. By default, the output is printed to the console.

```python
# Redirecting print output to a file
with open("output.txt", "w") as file:
    print("Hello, world!", file=file)
# This writes "Hello, world!" to the file "output.txt"
```