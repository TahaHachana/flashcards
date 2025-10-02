## Match Guards

What is a match guard and how is it used?

---

A guard is an `if` condition after a pattern. It refines when the arm applies:

```rust
match n {
    x if x % 2 == 0 => println!("{x} is even"),
    _ => println!("odd"),
}
```

