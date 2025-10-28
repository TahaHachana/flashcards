## Unwrap Family Comparison

Compare the different unwrap-related methods and when to use each.

---

| Method | Panics? | Use Case |
|--------|---------|----------|
| `unwrap()` | Yes | Tests, proven invariants (but prefer expect) |
| `expect("msg")` | Yes | Proven invariants with documentation |
| `unwrap_or(val)` | No | Safe default available |
| `unwrap_or_else(fn)` | No | Computed default, with logging |
| `unwrap_or_default()` | No | Type has reasonable Default |
| `?` operator | No | Error propagation (preferred) |
| `match` / `if let` | No | Explicit error handling |

**Priority:**
1. `?` for error propagation
2. `unwrap_or*` for defaults
3. `match` for custom handling
4. `expect()` for documented invariants
5. `unwrap()` only in tests

