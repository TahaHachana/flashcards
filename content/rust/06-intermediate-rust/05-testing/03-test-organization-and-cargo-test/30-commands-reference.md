## Essential Commands Quick Reference

What are the most essential `cargo test` commands to remember?

---

Core commands:

```bash
# Run all tests
cargo test

# Run specific test/module
cargo test test_name

# Show output for passing tests
cargo test -- --nocapture

# Run sequentially (for debugging)
cargo test -- --test-threads=1

# Combine filter and options
cargo test my_test -- --test-threads=1 --nocapture

# Run ignored tests
cargo test -- --ignored
cargo test -- --include-ignored

# Debug with backtrace
RUST_BACKTRACE=1 cargo test

# Only unit tests
cargo test --lib

# Quiet mode
cargo test -q

# Release mode
cargo test --release
```

Remember the structure:
```
cargo test [filter] -- [options]
           ↑           ↑
           Before      After separator
```

Most used: `cargo test test_name -- --nocapture`

