# first_word Function

How do you implement `first_word` to return a string slice instead of an index?

---

Return a `&str` tied to the original string by scanning for the first space:

```rust
fn first_word(s: &str) -> &str {
    let bytes = s.as_bytes();
    for (i, &b) in bytes.iter().enumerate() {
        if b == b' ' {
            return &s[..i];
        }
    }
    &s[..]
}

fn main() {
    let word = first_word("hello world");
    println!("First word: {}", word);
}
```