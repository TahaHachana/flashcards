## Accessing Characters with chars

How do you access the first, nth, or iterate over characters in a string?

---

```rust
let s = String::from("hello");

// First character
let first = s.chars().next();  // Some('h')

// Nth character (0-indexed)
let third = s.chars().nth(2);  // Some('l')

// Iterate over all characters
for ch in s.chars() {
    println!("{}", ch);
}
```
Note: nth() is O(n) because it must scan previous characters.

