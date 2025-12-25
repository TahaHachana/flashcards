## Tests Sharing Mutable State Problem

What problem occurs when tests share mutable state and how do you fix it?

---

Problem: Non-deterministic failures in parallel execution:

```rust
use std::sync::Mutex;

lazy_static! {
    static ref COUNTER: Mutex<i32> = Mutex::new(0);
}

#[test]
fn test_a() {
    *COUNTER.lock().unwrap() += 1;
    assert_eq!(*COUNTER.lock().unwrap(), 1);  // Fails randomly
}

#[test]
fn test_b() {
    *COUNTER.lock().unwrap() += 1;
    assert_eq!(*COUNTER.lock().unwrap(), 1);  // Fails randomly
}
```

Solutions:

1. Make tests independent (best):
```rust
#[test]
fn test_a() {
    let mut counter = 0;  // Local state
    counter += 1;
    assert_eq!(counter, 1);  // Always passes
}
```

2. Run sequentially (workaround):
```bash
cargo test -- --test-threads=1
```

Always prefer independent tests!

