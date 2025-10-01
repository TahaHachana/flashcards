## Shadowing In Inner Scopes

How does shadowing behave in nested scopes?

---

Shadowing can apply within inner scopes.
The inner binding only exists inside that scope.

```rust
fn main() {
    let x = 6;
    {
        let x = x * 2;
        println!("Inner x = {x}"); // 12
    }
    println!("Outer x = {x}"); // 6
}
```

