## Chars Iterator

What does the chars() method do and what does each iteration give you?

---

chars() iterates over Unicode scalar values (characters):
```rust
let s = String::from("hello");
for ch in s.chars() {
    println!("{}", ch);
}
// Prints: h, e, l, l, o
```
Each iteration gives you a char (4-byte Unicode scalar value). Use this when working with text and characters.

