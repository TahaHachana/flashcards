## Accessing Bytes with bytes

How do you access raw bytes in a string and when should you use this?

---

```rust
let s = String::from("hello");
for byte in s.bytes() {
    println!("{}", byte);  // 104, 101, 108, 108, 111
}
```
Use bytes() for binary data or low-level processing where you need the raw UTF-8 bytes rather than characters. Each iteration gives you a u8.

