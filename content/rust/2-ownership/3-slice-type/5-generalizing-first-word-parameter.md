# Generalizing first_word Parameter

How can you make `first_word` accept both `&String` and `&str`?

---

Define the parameter as `&str`; Rust will coerce `&String` to `&str` automatically:

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
    let my_string = String::from("hello world");
    println!("{}", first_word(&my_string));    // works
    println!("{}", first_word("hello world")); // also works
}
```