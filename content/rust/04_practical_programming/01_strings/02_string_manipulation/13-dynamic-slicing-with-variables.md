## Dynamic Slicing with Variables

How can you create slices based on runtime values? Show an example.

---

```rust
let s = String::from("hello world");
let space_index = s.find(' ').unwrap();

let first_word = &s[..space_index];
let second_word = &s[space_index + 1..];
```
You can use variables in slice ranges to create dynamic slices based on runtime calculations, like finding delimiters or search positions.

