## Finding Character Positions

How do you find the position of a specific character in a string?

---

```rust
let s = String::from("hello world");

// Find position
if let Some(pos) = s.chars().position(|c| c == 'w') {
    println!("Found 'w' at position {}", pos);  // 6
}

// Check if contains
let has_o = s.chars().any(|c| c == 'o');
```
Use position() to find the index, or any() to check existence. Both work on the chars() iterator.

