## Common String Methods - Length and Empty

How do you check a string's length and whether it's empty?

---

```rust
let mut s = String::from("  hello  ");
s.len();        // 9 (includes spaces, returns byte count)
s.is_empty();   // false

s.clear();      // Makes string empty
s.is_empty();   // true
s.len();        // 0
```
len() returns byte count (not character count), is_empty() checks if length is zero.

