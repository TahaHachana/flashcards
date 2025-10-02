## Alternation And Ranges

How can you match multiple values or a numeric range in one arm?

---

* Use `|` for alternation.
* Use `..=` for inclusive ranges.

```rust
match n {
    1 | 2 => println!("one or two"),
    3..=5 => println!("three through five"),
    _ => println!("other"),
}
```

