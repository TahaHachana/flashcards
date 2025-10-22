## Array Index Out of Bounds

What is the array index out of bounds problem, and what are its consequences?

---

Problem: Accessing A[i] when i < l or i > u (outside valid index range)

Consequences:
- Undefined behavior
- Program crash or segmentation fault
- Memory corruption
- Security vulnerabilities
- Accessing or modifying unrelated data

Solution: Always validate indices before access
- Check: l ≤ i ≤ u before accessing A[i]
- Use bounds-checking functions when available
- Many modern languages provide automatic bounds checking

