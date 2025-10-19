## Clone Explicit Copying

How do you explicitly duplicate a non-Copy type?

---

Use .clone() to create a deep copy. This allocates new memory and copies all data.

```rust
let s1 = String::from("hello");
let s2 = s1.clone();
println!("{} {}", s1, s2);  // ✅ Both valid
```

