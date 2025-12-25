## Tests Directory Location and Structure

What is the correct structure for the integration tests directory and what are the rules?

---

Structure:
```
my_project/
├── Cargo.toml
├── src/
│   └── lib.rs
└── tests/              # Must be named exactly 'tests/'
    ├── integration_test.rs
    ├── common/         # Subdirectory for shared utilities
    │   └── mod.rs
    └── another_test.rs
```

Rules:
1. Must be named exactly `tests/` at project root
2. Each `.rs` file becomes a separate test binary
3. Cargo automatically compiles files during `cargo test`
4. No `#[cfg(test)]` needed (entire file is a test)
5. Tests must import the crate like external users

