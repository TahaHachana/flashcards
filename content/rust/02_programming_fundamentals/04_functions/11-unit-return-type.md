## Unit Return Type

What is the implicit return type for functions that don't return a value?

---

The unit type (), though it's usually omitted from the signature.

```rust
fn print_msg(msg: &str) {
    println!("{}", msg);
}  // Implicitly returns ()

// Equivalent to:
fn print_msg(msg: &str) -> () { }
```

