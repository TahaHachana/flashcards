## Enumerating Characters with Index

How do you iterate over characters while also getting their position/index?

---

```rust
let s = String::from("hello");
for (i, ch) in s.chars().enumerate() {
    println!("Character {} is {}", i, ch);
}
// Character 0 is h
// Character 1 is e
// ...
```
Use enumerate() on the chars() iterator to get (index, character) tuples.

