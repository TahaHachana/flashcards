# Reading a File Line by Line

```python
# Open a file in read mode
file = open("example.txt", "r")

# Read and print each line in the file
for line in file:
    print(line.strip())

# Close the file
file.close()
```