## First Word Pattern

How do you implement a function that returns the first word of a string?

---

```rust
fn first_word(s: &str) -> &str {
    let bytes = s.as_bytes();
    for (i, &byte) in bytes.iter().enumerate() {
        if byte == b' ' {
            return &s[0..i];
        }
    }
    &s[..]  // Return whole string if no space
}
```
Iterate over bytes to find the first space, return slice up to that point, or entire string if no space found.

