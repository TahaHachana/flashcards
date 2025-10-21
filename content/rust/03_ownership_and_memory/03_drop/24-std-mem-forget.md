## std::mem::forget

How do you prevent drop from running?

---

Use std::mem::forget. This leaks memory and should only be used for FFI, low-level abstractions, or specific unsafe scenarios.

```rust
let s = String::from("hello");
std::mem::forget(s);  // Drop NOT called
```

