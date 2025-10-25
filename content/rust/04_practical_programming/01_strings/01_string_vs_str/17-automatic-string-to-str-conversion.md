## Automatic String to &str Conversion

When does String automatically convert to &str?

---

Automatic conversion happens:
1. When passing &String to function expecting &str
2. Through deref coercion
3. When explicitly borrowing with &

Example:
```rust
fn process(text: &str) { }
let s = String::from("hello");
process(&s);  // Implicit conversion through borrowing
```

