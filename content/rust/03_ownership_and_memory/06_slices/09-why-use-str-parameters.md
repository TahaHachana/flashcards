## Why Use &str Parameters

Why use &str instead of &String for function parameters?

---

More flexible. Works with String references (through deref coercion), string literals, and slices. Best practice for functions that only read strings.

```rust
fn process(s: &str) { }  // Works with all string types
```

