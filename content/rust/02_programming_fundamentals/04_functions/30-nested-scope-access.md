## Nested Scope Access

Can inner scopes access variables from outer scopes?

---

Yes. Inner scopes can access outer scope variables, but outer scopes cannot access inner scope variables.

```rust
fn outer() {
    let x = 5;
    {
        println!("{}", x);  // ✅ Can access x
        let y = 10;
    }
    println!("{}", y);  // ❌ Error: y out of scope
}
```

