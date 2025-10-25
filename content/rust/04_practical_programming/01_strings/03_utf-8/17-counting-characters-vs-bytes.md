## Counting Characters vs Bytes

How do you correctly count both bytes and characters in a string?

---

```rust
let s = String::from("Hello, 世界!");

// Byte count (O(1))
println!("Bytes: {}", s.len());  // 14

// Character count (O(n))
println!("Chars: {}", s.chars().count());  // 9
```
Always distinguish: len() for bytes (fast), chars().count() for characters (requires scanning).

