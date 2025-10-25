## String Ownership and Move Semantics

What happens to s1 in this code and why?
```rust
let s1 = String::from("hello");
let s2 = s1;
```

---

s1 becomes invalid because String owns its data and follows move semantics. When s2 is assigned, ownership moves from s1 to s2. s1 can no longer be used. When s2 goes out of scope, the heap memory is freed. This prevents double-free errors.

