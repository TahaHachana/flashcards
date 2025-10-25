## Take First N Characters

How do you extract the first n characters from a string?

---

```rust
fn take_chars(s: &str, n: usize) -> String {
    s.chars().take(n).collect()
}

let s = "你好世界";
println!("{}", take_chars(s, 2));  // "你好"
```
Use chars().take(n).collect() to safely get first n characters regardless of byte lengths.

