## Doc Test no_run Attribute

When and why should you use the `no_run` attribute in doc tests?

---

Use `no_run` when code should compile but not execute:

```rust
/// # Examples
///
/// ```no_run
/// // Infinite loop - compiles but shouldn't run
/// loop {
///     process_events();
/// }
/// ```

/// ```no_run
/// // Requires external resources
/// let data = fetch_from_api("https://example.com");
/// ```

/// ```no_run
/// // Has side effects (file I/O)
/// std::fs::write("output.txt", "data").unwrap();
/// ```
```

Use when:
- Example has side effects (network, files, database)
- Example is an infinite loop
- Example requires external resources
- Example would be slow to run

Code is still type-checked and compiled, ensuring correctness without execution.

