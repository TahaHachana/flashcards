## Copy Trait and Stack Data

Why can stack-only types implement the Copy trait but heap types cannot?

---

Stack types are cheap to duplicate (just copy bytes). Heap types would require duplicating heap allocations, which is expensive. Moving ownership instead of copying prevents double-free bugs.

```rust
let x = 5; let y = x;  // Copy: both valid
let s1 = String::from("hi"); let s2 = s1;  // Move: s1 invalid
```

