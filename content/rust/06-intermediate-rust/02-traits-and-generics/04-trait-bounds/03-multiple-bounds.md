## Multiple Trait Bounds

How do you specify that a generic type must implement multiple traits?

---

Use the `+` operator to combine multiple trait bounds:

```rust
fn process<T: Debug + Clone + PartialEq>(value: T) {
    println!("{:?}", value);      // Uses Debug
    let copy = value.clone();     // Uses Clone
    assert!(value == copy);       // Uses PartialEq
}
```

All traits separated by `+` must be implemented by the type.

