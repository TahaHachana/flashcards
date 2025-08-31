# The Copy Trait

What is the `Copy` trait and which types implement it?

---

Types with fixed size (no heap data) implement `Copy`. Assignment makes a bitwise copy; the original remains valid.  

```rust
let a = 5;     // i32 implements Copy
let b = a;     // a is still valid
println!("a = {}, b = {}", a, b);
```

Common `Copy` types: integers, booleans, floats, `char`, and tuples of `Copy` types.
