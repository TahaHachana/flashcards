# Integer Overflow Handling

How does Rust handle integer overflow in debug vs release mode?

---

- **Debug mode**: Panics when integer overflow occurs
- **Release mode**: Wraps around (two's complement wrapping)