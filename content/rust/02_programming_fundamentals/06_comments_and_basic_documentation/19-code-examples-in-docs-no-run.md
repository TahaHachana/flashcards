## Code Examples in Docs - no_run

How do you include examples in documentation that shouldn't be executed during testing?

---

Use ```no_run to mark examples that shouldn't run.

```rust
/// # Examples
/// ```no_run
/// // Requires external setup
/// connect_to_database();
/// ```
```

