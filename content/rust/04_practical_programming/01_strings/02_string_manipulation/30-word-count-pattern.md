## Word Count Pattern

How do you implement a word count function?

---

```rust
fn word_count(s: &str) -> usize {
    s.split_whitespace().count()
}

let text = "hello world from rust";
println!("{} words", word_count(text));  // 4 words
```
Use split_whitespace() to get an iterator over words, then count() to get the total.

