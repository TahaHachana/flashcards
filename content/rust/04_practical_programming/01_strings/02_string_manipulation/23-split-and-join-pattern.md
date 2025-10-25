## Split and Join Pattern

How do you split a string by a delimiter and then join the parts with a different delimiter?

---

```rust
let s = String::from("apple,banana,cherry");
let words: Vec<&str> = s.split(',').collect();
// words: ["apple", "banana", "cherry"]

let joined = words.join(" - ");
// "apple - banana - cherry"
```
Use split() to break into parts (returns iterator), collect() into Vec, then join() with new delimiter.

