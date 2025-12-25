## Running Specific Test Types

What commands run specific types of tests (unit, integration, doc)?

---

```bash
# Run only unit tests (in lib/binary)
cargo test --lib

# Run only integration tests
cargo test --test '*'

# Run specific integration test file
cargo test --test integration_test

# Run only doc tests
cargo test --doc
```

Examples:
```bash
# During development (fast feedback)
cargo test --lib

# Before commit (comprehensive)
cargo test              # All tests
cargo test --doc        # Then doc tests
cargo test --test '*'   # Then integration tests
```

This allows targeted testing during different development phases.

