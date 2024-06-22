# File Modes

* `'r'` - Read mode (default). Opens a file for reading.
* `'w'` - Write mode. Opens a file for writing (creates a new file or truncates an existing file).
* `'a'` - Append mode. Opens a file for appending (creates a new file if it doesn't exist).
* `'b'` - Binary mode. Can be added to other modes (e.g., 'rb', 'wb') for binary files.
* `'t'` - Text mode (default). Can be added to other modes (e.g., 'rt', 'wt').

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