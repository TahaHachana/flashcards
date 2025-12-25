## Integration Tests Summary Table

Summarize the key characteristics of integration tests in a comparison format.

---

| Aspect | Library Crate | Binary Crate |
|--------|---------------|--------------|
| File | `src/lib.rs` | `src/main.rs` (only) |
| Integration testable | ✅ Yes, directly | ❌ No |
| Public exports | ✅ Via `pub` | ❌ None |
| Import in tests | `use my_lib;` | Must split to lib first |
| Access | Public items only | N/A |

Integration test characteristics:
- **Location**: `tests/` directory
- **Compilation**: Each file = separate binary
- **Visibility**: Public APIs only
- **Purpose**: Test component integration
- **Perspective**: External user
- **Organization**: Feature-based files
- **Shared code**: Use subdirectories (`tests/common/`)
- **Speed**: Slower than unit tests
- **Quantity**: Fewer, more comprehensive

Remember: Split binaries into lib.rs + thin main.rs for testability.

