## Transforming Characters with Map

How do you transform each character in a string?

---

```rust
let s = String::from("hello");
let upper: String = s.chars()
    .map(|c| c.to_ascii_uppercase())
    .collect();
println!("{}", upper);  // "HELLO"
```
Chain chars(), map() with a transformation function, and collect() into a new String. Map applies the transformation to each character.

