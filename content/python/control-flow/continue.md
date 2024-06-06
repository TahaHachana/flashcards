# Continue

The continue statement in Python is used to skip the rest of the code inside a loop for the current iteration and move to the next iteration of the loop.

```python
# Using continue in a for loop:
for i in range(10):
    if i % 2 == 0:  # Skip even numbers
        continue
    print(i)

# Using continue in a while loop:
count = 0
while count < 10:
    count += 1
    if count % 2 == 0:  # Skip even numbers
        continue
    print(count)
```