## Bytes Iterator

What does the bytes() method do and what does each iteration give you?

---

bytes() iterates over raw bytes:
```rust
let s = String::from("hello");
for byte in s.bytes() {
    println!("{}", byte);
}
// Prints: 104, 101, 108, 108, 111 (ASCII values)
```
Each iteration gives you a u8. Use this when working with raw data rather than text characters.

