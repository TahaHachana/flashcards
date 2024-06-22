# Appending to a File

In Python, you can append to a file using the `write()` method with the `a` mode.

---

```python
# Open a file in append mode
file = open("example.txt", "a")

# Append some content to the file
file.write("\nAppended text.")

# Close the file
file.close()
```