# Conditional Statements

The if conditional statement in Python is used to execute a block of code only if a specified condition is true. It can be extended with elif (else if) and else clauses to handle multiple conditions and provide alternative execution paths.

---

```python
a = 10
b = 3

# Basic if statement
if a > b:
    print("a is greater than b")

# if-elif-else statement
if a < b:
    print("a is less than b")
elif a == b:
    print("a is equal to b")
else:
    print("a is greater than b")
```