## String Growability

How can you grow a String dynamically and what happens if it exceeds capacity?

---

Use push() to add a character or push_str() to add a string slice:
```rust
let mut s = String::from("hello");
s.push(' ');
s.push_str("world");
```
If the string exceeds its capacity, Rust automatically reallocates with more space.

