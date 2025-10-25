## Reverse String with UTF-8

How do you reverse a string while correctly handling multi-byte characters?

---

```rust
fn reverse_string(s: &str) -> String {
    s.chars().rev().collect()
}

let s = "hello";
println!("{}", reverse_string(s));  // "olleh"

let s = "你好";
println!("{}", reverse_string(s));  // "好你"
```
chars().rev() reverses character by character, maintaining UTF-8 validity.

