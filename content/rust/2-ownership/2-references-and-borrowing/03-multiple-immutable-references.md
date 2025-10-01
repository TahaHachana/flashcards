## Multiple Immutable References

Can you have multiple immutable references to the same value?

---

Yes. Multiple `&T` immutable references are allowed simultaneously because they only read the value.

```rust
let s = String::from("hello");
let r1 = &s;
let r2 = &s;
println!("{r1}, {r2}");
```

