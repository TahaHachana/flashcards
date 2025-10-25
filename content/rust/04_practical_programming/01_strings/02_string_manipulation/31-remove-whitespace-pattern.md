## Remove Whitespace Pattern

How do you remove all whitespace characters from a string?

---

```rust
let s = "h e l l o";
let no_spaces: String = s.chars()
    .filter(|c| !c.is_whitespace())
    .collect();
println!("{}", no_spaces);  // "hello"
```
Iterate with chars(), filter out whitespace with is_whitespace(), then collect into String.

