## Creating String Slices

How do you create a string slice?

---

Use range syntax in square brackets.

```rust
let s = String::from("hello world");
let hello = &s[0..5];   // "hello"
let world = &s[6..11];  // "world"
```

