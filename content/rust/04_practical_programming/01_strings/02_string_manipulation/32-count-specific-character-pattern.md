## Count Specific Character Pattern

How do you count how many times a specific character appears in a string?

---

```rust
let s = "hello world";
let count = s.chars().filter(|&c| c == 'l').count();
println!("{} 'l' characters", count);  // 3 'l' characters
```
Use chars() to iterate, filter() to keep only matching characters, then count() the results.

