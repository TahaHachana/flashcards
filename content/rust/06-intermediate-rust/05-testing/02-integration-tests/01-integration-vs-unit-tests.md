## Integration Tests vs Unit Tests

What are the key differences between integration tests and unit tests in Rust?

---

Unit tests:
- Live in `#[cfg(test)]` modules within source files
- Can access private functions and internal state
- Test implementation details
- Part of the same compilation unit
- Many tests, fast execution

Integration tests:
- Live in separate `tests/` directory
- Can only access public APIs
- Test from external user perspective
- Each file is a separate binary
- Fewer tests, slower execution

Integration tests treat your crate as a black box and verify that modules work together correctly.

