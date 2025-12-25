## Test Independence Principle

Why must tests be independent and what problems arise from test dependencies?

---

Tests must not depend on:
- Execution order
- Shared mutable state
- Results from other tests

Bad (dependent tests):
```rust
static mut COUNTER: i32 = 0;

#[test]
fn test_first() {
    unsafe { COUNTER += 1; }
    assert_eq!(unsafe { COUNTER }, 1);
}

#[test]
fn test_second() {  // Might fail!
    assert_eq!(unsafe { COUNTER }, 1);
}
```

Good (independent tests):
```rust
#[test]
fn test_increment() {
    let mut counter = 0;
    counter += 1;
    assert_eq!(counter, 1);
}

#[test]
fn test_decrement() {
    let mut counter = 10;
    counter -= 1;
    assert_eq!(counter, 9);
}
```

Why: Tests run in parallel and in non-deterministic order. Dependencies cause flaky tests.

