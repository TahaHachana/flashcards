## Command Structure Double Dash

Explain the structure of `cargo test` commands with the double dash separator.

---

Structure:
```
cargo test [CARGO_OPTIONS] [FILTER] -- [TEST_BINARY_OPTIONS]
           ↑                ↑         ↑  ↑
           |                |         |  Options for test binary
           |                |         Separator
           |                Test filter
           Options for cargo
```

Examples:

```bash
# Filter only (no dash needed)
cargo test addition

# Test binary option (needs --)
cargo test -- --nocapture

# Both filter and test option
cargo test addition -- --nocapture

# Multiple test options
cargo test -- --test-threads=1 --nocapture

# Cargo option + filter + test options
cargo test --lib addition -- --nocapture
```

Common mistake:
```bash
cargo test --nocapture  # ❌ Error: cargo doesn't recognize
cargo test -- --nocapture  # ✅ Correct: test binary interprets
```

