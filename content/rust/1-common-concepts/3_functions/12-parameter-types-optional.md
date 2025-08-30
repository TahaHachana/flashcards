# Parameter Types Optional

Are function parameter types optional in Rust?

---

No! Types must be **explicitly declared** for all parameters. This is different from variables where types can often be inferred. Example:
```rust
fn greet(name: String) { // Must specify String type
    println!("Hello, {name}!");
}
```