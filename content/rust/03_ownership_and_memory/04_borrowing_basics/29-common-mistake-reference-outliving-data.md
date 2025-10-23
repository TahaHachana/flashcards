## Common Mistake Reference Outliving Data

Can a reference outlive the data it points to?

---

No. The compiler prevents dangling references.

```rust
let r;
{
    let s = String::from("hello");
    r = &s;  // ❌ Error: s doesn't live long enough
}
println!("{}", r);  // Would be dangling
```

