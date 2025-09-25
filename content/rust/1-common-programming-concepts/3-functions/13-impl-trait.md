## impl Trait Syntax

What is the `impl Trait` syntax used for in function parameters and return types?

---

It provides shorthand for generics:

* In parameters, it accepts any type implementing the trait.
* In return values, it hides the concrete type but guarantees it implements the trait.

Example:

```rust
fn log_line(item: impl std::fmt::Display) {
    println!("{item}");
}
```

