## Common Development Patterns

What are common `cargo test` patterns for different development scenarios?

---

**Quick iteration** (working on specific test):
```bash
cargo test my_test -- --nocapture
```

**Debugging failure** (single-threaded with output):
```bash
cargo test failing_test -- --test-threads=1 --nocapture
RUST_BACKTRACE=1 cargo test failing_test
```

**Pre-commit check** (comprehensive):
```bash
cargo test -- --include-ignored
cargo test --release
```

**CI/CD pipeline**:
```bash
cargo test --verbose
cargo test --lib
cargo test --doc
cargo test --test '*'
```

**Fast feedback loop** (unit tests only):
```bash
cargo test --lib
```

Adapt pattern to your current task for efficient testing.

