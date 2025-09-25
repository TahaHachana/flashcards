## Multiple Parameters

How do you define multiple parameters in a Rust function?

---

Separate parameter declarations with commas, and specify the type for each.

Example:
```rust
fn print_labeled_measurement(value: i32, unit_label: char) {
    println!("The measurement is: {value}{unit_label}");
}
```

