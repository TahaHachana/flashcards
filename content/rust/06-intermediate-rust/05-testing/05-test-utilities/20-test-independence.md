## Test Independence Principle

Why must tests be independent and how do you ensure this?

---

Tests must be independent because they:
- Run in **non-deterministic order**
- Run in **parallel** by default
- Shared state causes **flaky tests**

Bad (dependent tests):
```rust
static mut STATE: i32 = 0;

#[test]
fn test_a() {
    unsafe { STATE = 5; }
    assert_eq!(unsafe { STATE }, 5);
}

#[test]
fn test_b() {
    // ❌ Fails if test_a runs first
    assert_eq!(unsafe { STATE }, 0);
}
```

Good (independent tests):
```rust
#[test]
fn test_a() {
    let state = 5;
    assert_eq!(state, 5);
}

#[test]
fn test_b() {
    let state = 0;
    assert_eq!(state, 0);
}
```

Principles:
- Each test creates own state
- No shared mutable globals
- Tests don't depend on execution order
- Setup and cleanup within each test
- Use `--test-threads=1` only for debugging

Independent tests are reliable tests.

