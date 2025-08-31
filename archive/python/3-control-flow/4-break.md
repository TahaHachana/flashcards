# Break

The break statement in Python is used to exit a loop prematurely, skipping any remaining iterations even if the loop's condition has not been met.

---

```python
# Using break in a for loop:
for i in range(10):
    if i == 5:
        break
    print(i)

# Using break in a while loop:
count = 0
while count < 10:
    if count == 5:
        break
    print(count)
    count += 1
```