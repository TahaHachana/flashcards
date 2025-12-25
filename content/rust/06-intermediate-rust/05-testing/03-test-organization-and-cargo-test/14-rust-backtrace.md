## RUST_BACKTRACE Environment Variable

How do you enable backtraces for failing tests and what does it show?

---

Enable with `RUST_BACKTRACE` environment variable:

```bash
# Show backtrace
RUST_BACKTRACE=1 cargo test

# Show full backtrace
RUST_BACKTRACE=full cargo test
```

Example:
```rust
#[test]
fn test_panic() {
    let v = vec![1, 2];
    let _ = v[5];  // Panics
}
```

With backtrace:
```
thread 'test_panic' panicked at src/lib.rs:4:13:
index out of bounds: the len is 2 but the index is 5
stack backtrace:
   0: rust_begin_unwind
   1: core::panicking::panic_fmt
   2: core::panicking::panic_bounds_check
   3: my_crate::tests::test_panic
   ... (more frames)
```

Shows the call stack leading to the panic, useful for debugging.

