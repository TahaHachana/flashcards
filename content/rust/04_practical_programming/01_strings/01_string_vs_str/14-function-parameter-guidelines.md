## Function Parameter Guidelines

Why should you prefer &str over &String for function parameters?

---

&str is more flexible because it works with String, &str, and string literals:
```rust
fn process(text: &str) { }  // Flexible

process("Alice");                // Literal
process(&String::from("Bob"));   // String
process(&s[..]);                 // Slice
```
&String requires specifically a String, limiting what callers can pass. &str provides maximum flexibility without requiring ownership.

