# Avoiding Dangling References

How do you avoid dangling references when you need to return owned data?

---

Return the owned value, transferring ownership to the caller instead of a reference.

```rust
fn no_dangle() -> String {
    let s = String::from("hello");
    s
}

fn main() {
    let s = no_dangle();
    println!("{}", s);
}
```