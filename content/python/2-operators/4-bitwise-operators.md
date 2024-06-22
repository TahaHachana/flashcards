# Bitwise Operators

Bitwise operators in Python are used to perform bit-level operations on integer values. The primary bitwise operators include &, |, ^, ~, <<, and >>.

---

```python
a = 10  # Binary: 1010
b = 3   # Binary: 0011

# Bitwise AND
print(a & b)  # Output: 2  (Binary: 0010)

# Bitwise OR
print(a | b)  # Output: 11 (Binary: 1011)

# Bitwise XOR
print(a ^ b)  # Output: 9  (Binary: 1001)

# Bitwise NOT
print(~a)     # Output: -11 (Binary: ...11110101, two's complement representation)

# Bitwise left shift
print(a << 1)  # Output: 20 (Binary: 10100)

# Bitwise right shift
print(a >> 1)  # Output: 5  (Binary: 0101)
```