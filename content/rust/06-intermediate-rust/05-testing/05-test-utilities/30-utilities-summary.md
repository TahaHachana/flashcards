## Test Utilities Summary

Summarize the key test utilities and their purposes.

---

Attributes:
- `#[should_panic]` - Test panics (with `expected` for message)
- `#[ignore]` - Skip slow/external tests

Setup patterns:
- Helper functions - Simple reusable setup
- Fixtures - Complex test environments
- Builders - Flexible test data
- Drop trait - Automatic cleanup

Best practices:
1. **Independence** - No shared mutable state
2. **RAII cleanup** - Use Drop for reliability
3. **Clear naming** - Descriptive helper names
4. **Documentation** - Comment complex helpers
5. **Error messages** - Provide context
6. **Organization** - Group by feature

Common patterns:
- File systems: TempDir with Drop
- Databases: Transaction with rollback
- Servers: MockServer with shutdown
- Resources: Guard with cleanup

Running:
```bash
cargo test -- --ignored      # Only ignored
cargo test -- --include-ignored  # All
```

Key principle: Tests should be independent, reliable, and maintainable.

