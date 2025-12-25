## Running Tests Commands

How do you run tests in Rust, and what are some useful filtering options?

---

Basic commands:
```bash
cargo test              # Run all tests
cargo test test_name    # Run specific test
cargo test addition     # Run tests matching pattern
```

Useful options:
```bash
# Show println! output for passing tests
cargo test -- --nocapture

# Run tests in specific module
cargo test tests::addition

# Run single-threaded (for debugging)
cargo test -- --test-threads=1
```

In Rust Playground:
- Click "···" menu next to RUN
- Select "TEST" instead of "RUN"

