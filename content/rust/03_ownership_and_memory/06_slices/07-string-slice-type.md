## String Slice Type

What is the type of a string slice?

---

&str (string slice). An immutable reference to part of a string.

```rust
let s = String::from("hello");
let slice: &str = &s[0..2];
```

