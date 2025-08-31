# Open()

The `open()` function in Python is used to open a file and return a corresponding file object. This function is used for reading, writing, and appending data to files. The syntax is `open(file, mode)`, where file is the name (and path) of the file and mode specifies the mode in which the file is opened.

---

```python
# Open a file in read mode
file = open("example.txt", "r")

# Read the entire content of the file
content = file.read()
print(content)

# Close the file
file.close()
```