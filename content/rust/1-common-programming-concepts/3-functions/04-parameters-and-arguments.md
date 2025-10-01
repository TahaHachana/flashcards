## Parameters And Arguments

What is the difference between parameters and arguments in Rust functions?

---

* **Parameters**: Variables defined in the function signature.
* **Arguments**: Actual values passed when calling the function.

```rust
fn print_num(x: i32) {  // parameter
    println!("{x}");
}

fn main() {
    print_num(5);       // argument
}
```

