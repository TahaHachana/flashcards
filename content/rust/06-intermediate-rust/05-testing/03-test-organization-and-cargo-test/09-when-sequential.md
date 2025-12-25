## When to Use Sequential Execution

When should you run tests sequentially with `--test-threads=1`?

---

Use `--test-threads=1` when:

1. **Tests share state** (not ideal, but happens):
```rust
static mut COUNTER: i32 = 0;

#[test]
fn test_a() {
    unsafe { COUNTER += 1; }
    assert_eq!(unsafe { COUNTER }, 1);  // Fails in parallel
}
```

2. **Resource conflicts**:
```rust
#[test]
fn test_file_write() {
    fs::write("test.txt", "data").unwrap();
}

#[test]
fn test_file_read() {
    let content = fs::read_to_string("test.txt").unwrap();
    // May conflict if both run simultaneously
}
```

3. **Debugging** (clearer output):
```bash
cargo test -- --test-threads=1 --nocapture
# Output not interleaved
```

4. **Limited resources** (ports, database connections)

Better solution: Make tests independent when possible!

