# Fix Constant Declaration

What's wrong with this constant declaration?
```rust
const RESULT = get_value();
```

---

Constants must be set to compile-time constant expressions. Function calls are not allowed. Also missing type annotation. Should be:
```rust
const RESULT: i32 = 42;
```
