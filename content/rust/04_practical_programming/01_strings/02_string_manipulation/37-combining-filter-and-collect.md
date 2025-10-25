## Combining Filter and Collect

How do you extract only letters from a mixed alphanumeric string?

---

```rust
let s = String::from("a1b2c3");
let letters: String = s.chars()
    .filter(|c| c.is_alphabetic())
    .collect();
println!("{}", letters);  // "abc"
```
Chain chars() for character iteration, filter() with is_alphabetic() predicate, and collect() into a new String.

