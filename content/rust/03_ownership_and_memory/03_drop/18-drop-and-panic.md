## Drop and Panic

Does drop run if a panic occurs?

---

Yes. Rust unwinds the stack during panic, dropping values in reverse order. Exception: if panic occurs during drop, Rust aborts to prevent cascading failures.

```rust
// Even with panic, drops still run
let guard = Guard::new();
panic!("Error!");
// guard is still dropped during unwinding
```

