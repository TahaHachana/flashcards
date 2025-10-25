## Borrowing Slices from String

How can you create a &str that references part or all of a String?

---

```rust
let s = String::from("hello world");
let slice: &str = &s[0..5];  // Part: "hello"
let full: &str = &s;         // All: "hello world"
```
Use indexing with ranges for partial slices, or borrow the entire String with &s.

