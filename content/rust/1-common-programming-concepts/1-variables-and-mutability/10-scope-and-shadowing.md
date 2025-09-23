## Scope And Shadowing

How does scope affect shadowing in Rust?

---

Shadowing applies within the scope where the new variable is declared.
When the scope ends, the previous binding becomes visible again.

Note: inner scope shadowing does **not** update the outer variable — it only hides it temporarily.

```rust
let x = 5;
{
    let x = 10; // shadows outer x
    println!("{x}"); // 10
}
println!("{x}"); // 5
```

