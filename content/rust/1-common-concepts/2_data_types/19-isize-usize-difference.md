# isize/usize Difference

What's the difference between `isize`/`usize` and other integer types?

---

- `isize`/`usize` depend on the computer architecture:
  - 32 bits on 32-bit systems
  - 64 bits on 64-bit systems
- Primarily used for indexing collections
- Other integer types have fixed sizes regardless of architecture