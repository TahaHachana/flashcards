## Basic Trait Bound Syntax

What is the syntax for adding a trait bound to a generic type parameter?

---

Use a colon after the type parameter followed by the trait name:

```rust
fn function<T: TraitName>(param: T) {
    // T is constrained by TraitName
}

// Example:
fn debug_print<T: Debug>(value: T) {
    println!("{:?}", value);
}
```

The syntax `T: Debug` means "T is constrained by the Debug trait."

