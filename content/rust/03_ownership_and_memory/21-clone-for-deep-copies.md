## Clone for Deep Copies

How do you explicitly duplicate heap-allocated data?

---

Use .clone() to create a deep copy. This allocates new heap memory and copies all data.

```rust
let s1 = String::from("hello");
let s2 = s1.clone();  // Both valid now
println!("{} {}", s1, s2);  // ✅ Both work
```

