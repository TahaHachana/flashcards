## Parallel vs Sequential Execution

How do tests run by default, and how can you change this behavior?

---

Default: Tests run in **parallel** (concurrently)

```bash
# Default parallel execution
cargo test

# Sequential (one at a time)
cargo test -- --test-threads=1

# Custom thread count
cargo test -- --test-threads=4
```

Example timing:
```rust
#[test]
fn test_one() {
    sleep(Duration::from_secs(1));
}

#[test]
fn test_two() {
    sleep(Duration::from_secs(1));
}

#[test]
fn test_three() {
    sleep(Duration::from_secs(1));
}
```

Parallel: ~1 second total (all run together)
Sequential: ~3 seconds total (one after another)

Use `--test-threads=1` when tests share resources or for debugging.

