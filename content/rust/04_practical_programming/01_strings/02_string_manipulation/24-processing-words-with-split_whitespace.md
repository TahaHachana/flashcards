## Processing Words with Split_whitespace

How do you iterate over words in a string?

---

```rust
let s = String::from("hello world from rust");
for word in s.split_whitespace() {
    println!("{}", word.to_uppercase());
}
// HELLO
// WORLD
// FROM
// RUST
```
Use split_whitespace() to iterate over words, automatically handling any whitespace as delimiters.

