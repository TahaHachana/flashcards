## Nested Vector Syntax

What is the type of a vector containing vectors of strings? Give an example.

---

`Vec<Vec<String>>` - a vector of vectors.
Example:
```rust
let books: Vec<Vec<String>> = vec![
    vec![String::from("Book1"), String::from("Book2")],
    vec![String::from("Book3")],
];
```

