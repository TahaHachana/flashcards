## Combining Filter and Options

How do you combine test filtering with test binary options?

---

Place filter before `--`, options after:

```bash
# Filter + single option
cargo test addition -- --nocapture

# Filter + multiple options
cargo test addition -- --test-threads=1 --nocapture

# Cargo option + filter + test options
cargo test --lib addition -- --nocapture

# Multiple filters + options
cargo test add subtract -- --nocapture
```

Structure:
```
cargo test [cargo-opts] [filter] -- [test-opts]
```

Examples:
```bash
# Only run 'user' tests, show output, sequential
cargo test user -- --test-threads=1 --nocapture

# Run integration tests matching 'api', with backtrace
RUST_BACKTRACE=1 cargo test --test api_test api -- --nocapture
```

Remember: Everything after `--` goes to the test binary.

