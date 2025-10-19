## Temporary Ownership Pattern

How do you temporarily give ownership to a function then get it back?

---

Have the function return the value back.

```rust
fn process(s: String) -> String {
    // Use s
    s  // Give it back
}
let mut data = String::from("hello");
data = process(data);  // Move out, then back
```

