# For Loop Preference

Why is a `for` loop preferred over a `while` loop for iterating collections?

---

It's safer, more concise, and avoids index errors.

```rust
fn main() {
    let arr = [1, 2, 3];
    for val in arr {
        println!("{val}");
    }
}
```