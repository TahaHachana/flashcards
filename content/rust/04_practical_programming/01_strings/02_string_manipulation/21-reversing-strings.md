## Reversing Strings

How do you reverse a string in Rust?

---

```rust
let s = String::from("hello");
let reversed: String = s.chars().rev().collect();
println!("{}", reversed);  // "olleh"
```
Use chars() to iterate over characters, rev() to reverse the iterator, then collect() into a new String.

