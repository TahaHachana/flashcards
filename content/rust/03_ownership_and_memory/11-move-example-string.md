## Move Example String

What happens when you assign one String to another?

---

Ownership moves. The original variable becomes invalid and cannot be used. Only the new owner is valid.

```rust
let s1 = String::from("hello");
let s2 = s1;  // s1 is now invalid
println!("{}", s2);  // ✅ OK
println!("{}", s1);  // ❌ Error
```

