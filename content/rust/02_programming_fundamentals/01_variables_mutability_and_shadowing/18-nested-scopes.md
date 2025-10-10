## Nested Scopes

Can inner scopes access variables from outer scopes?

---

Yes. Inner scopes can access variables from outer scopes, but outer scopes cannot access variables from inner scopes.

```rust
let x = 5;
{
    let y = 10;
    println!("{} {}", x, y);  // ✅ Both valid
}
println!("{}", x);  // ✅ x still valid
println!("{}", y);  // ❌ Error: y out of scope
```

