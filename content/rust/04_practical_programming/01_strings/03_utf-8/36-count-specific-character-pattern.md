## Count Specific Character Pattern

How do you count occurrences of a specific character in a string?

---

```rust
fn count_char(s: &str, target: char) -> usize {
    s.chars().filter(|&c| c == target).count()
}

let s = "hello world";
println!("{}", count_char(s, 'l'));  // 3
```
Use chars() to iterate, filter() to keep matching characters, count() to get the total.

