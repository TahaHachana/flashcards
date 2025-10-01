## Initialization Requirement

Do variables in Rust need to be initialized before use?

---

Yes, all variables must be initialized before use.
Rust does not allow uninitialized variables.

```rust
fn main() {
    let x: i32;
    // println!("{x}"); // ❌ compile-time error: use of possibly uninitialized variable
}
```

