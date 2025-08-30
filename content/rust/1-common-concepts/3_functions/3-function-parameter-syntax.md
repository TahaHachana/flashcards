# Function Parameter Syntax

Complete this function definition with proper parameter syntax:
```rust
fn print_labeled_measurement(?, ?) {
    println!("The measurement is: {value}{unit_label}");
}
```

---

```rust
fn print_labeled_measurement(value: i32, unit_label: char) {
    println!("The measurement is: {value}{unit_label}");
}
```
Types must be explicitly declared for all parameters.
