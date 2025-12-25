## Shared State Anti-Pattern

Why is shared mutable state in tests problematic and what's the solution?

---

Problem: Non-deterministic failures with parallel tests:

```rust
use std::sync::Mutex;

lazy_static! {
    static ref COUNTER: Mutex<i32> = Mutex::new(0);
}

#[test]
fn test_a() {
    *COUNTER.lock().unwrap() = 0;
    *COUNTER.lock().unwrap() += 1;
    assert_eq!(*COUNTER.lock().unwrap(), 1);  // ❌ Fails if test_b runs concurrently
}

#[test]
fn test_b() {
    *COUNTER.lock().unwrap() = 0;
    *COUNTER.lock().unwrap() += 2;
    assert_eq!(*COUNTER.lock().unwrap(), 2);  // ❌ Fails if test_a runs concurrently
}
```

Solutions:

1. **Make tests independent** (best):
```rust
#[test]
fn test_a() {
    let mut counter = 0;
    counter += 1;
    assert_eq!(counter, 1);  // ✅ Always passes
}
```

2. **Run sequentially** (workaround):
```bash
cargo test -- --test-threads=1
```

3. **Use test-specific state**:
```rust
#[test]
fn test_a() {
    let ctx = TestContext::new();  // Isolated state
    ctx.counter += 1;
    assert_eq!(ctx.counter, 1);
}
```

Always prefer independent tests.

