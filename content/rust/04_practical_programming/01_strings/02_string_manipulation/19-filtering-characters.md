## Filtering Characters

How do you filter characters from a string based on a condition?

---

```rust
let s = String::from("h3ll0 w0rld");
let letters: String = s.chars()
    .filter(|c| c.is_alphabetic())
    .collect();
println!("{}", letters);  // "hllwrld"
```
Chain chars(), filter() with a predicate, and collect() into a new String. The filter removes non-alphabetic characters.

