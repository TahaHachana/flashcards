## When to Skip Doc Tests

When should you use the `ignore` attribute in doc tests?

---

Use `ignore` when example shouldn't run as a test:

```rust
/// # Examples
///
/// ```ignore
/// // This is pseudocode
/// let result = some_future_api();
/// ```

/// ```ignore
/// // This requires manual setup
/// // 1. Install PostgreSQL
/// // 2. Create database
/// // 3. Run migrations
/// let db = connect_to_database();
/// ```

/// ```ignore
/// // Platform-specific example (Windows only)
/// use windows::Win32::Foundation::HWND;
/// ```
```

Use when:
- Example is pseudocode/illustration
- Requires complex external setup
- Platform-specific (doesn't compile everywhere)
- Still in development

Note: Different from `#[ignore]` on unit tests. Doc test `ignore` is in the code fence.

Prefer `no_run` when possible (still type-checks).

