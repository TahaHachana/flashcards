# Assignment Operators

Assignment operators in Python are used to assign values to variables and can also perform operations before the assignment. The primary assignment operators include =, +=, -=, *=, /=, %=, //=, **=, &=, |=, ^=, <<=, and >>=.

---

```python
a = 10
b = 3

# Simple assignment
a = b        # a is now 3

# Add and assign
a += b       # a is now 6 (3 + 3)

# Subtract and assign
a -= b       # a is now 3 (6 - 3)

# Multiply and assign
a *= b       # a is now 9 (3 * 3)

# Divide and assign
a /= b       # a is now 3.0 (9 / 3)

# Modulus and assign
a %= b       # a is now 0.0 (3.0 % 3)

# Floor division and assign
a = 10       # reset a to 10
a //= b      # a is now 3 (10 // 3)

# Exponentiation and assign
a **= b      # a is now 27 (3 ** 3)

# Bitwise AND and assign
a &= b       # a is now 3 (27 & 3)

# Bitwise OR and assign
a |= b       # a is now 3 (3 | 3)

# Bitwise XOR and assign
a ^= b       # a is now 0 (3 ^ 3)

# Bitwise left shift and assign
a = 10       # reset a to 10
a <<= b      # a is now 80 (10 << 3)

# Bitwise right shift and assign
a >>= b      # a is now 10 (80 >> 3)
```