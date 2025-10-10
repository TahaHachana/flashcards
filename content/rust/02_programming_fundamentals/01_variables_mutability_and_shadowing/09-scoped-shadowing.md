## Scoped Shadowing

What happens to a shadowed variable when the inner scope ends?

---

The original variable becomes accessible again. Shadowing is scope-specific.

```rust
let x = 5;
{
    let x = x * 2;  // Shadows within block
    println!("{}", x);  // 10
}
println!("{}", x);  // 5 - original x is back
```

