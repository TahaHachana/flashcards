## Hidden Lines in Doc Tests

How do you hide setup code in documentation examples while still running it in tests?

---

Use `#` prefix for lines that run in tests but don't show in docs:

```rust
/// # Examples
///
/// ```
/// # use my_crate::Parser;
/// # let parser = Parser::new();
/// # let config = Config::default();
/// # parser.set_config(config);
/// // Users only see this:
/// let result = parser.parse("input");
/// assert_eq!(result, expected);
/// ```
```

In rendered docs, users see:
```rust
let result = parser.parse("input");
assert_eq!(result, expected);
```

In tests, full code (including hidden lines) executes.

Rules:
- Line must start with `# ` (hash + space)
- Hidden in docs, executed in tests
- Use for imports, setup, error handling

