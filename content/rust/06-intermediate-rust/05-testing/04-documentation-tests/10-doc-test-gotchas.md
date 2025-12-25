## Doc Test Expected Gotchas

What common mistakes occur when writing documentation tests?

---

Gotcha 1: Forgetting imports
```rust
/// ```
/// // ❌ Config not in scope
/// let config = Config::default();
/// ```
```
Solution: Add hidden import `# use my_crate::Config;`

Gotcha 2: Missing error handling
```rust
/// ```
/// let content = read_file("data.txt")?;  // ❌ Can't use ? outside fn
/// ```
```
Solution: Wrap in hidden main with Result return

Gotcha 3: Environment-specific code
```rust
/// ```
/// // ❌ Assumes file exists
/// let content = read_file("test.txt").unwrap();
/// ```
```
Solution: Use `no_run` or create file in hidden setup

Gotcha 4: Testing private functions
```rust
/// ```
/// // ❌ Can't access private
/// let result = my_crate::private_fn();
/// ```
```
Solution: Make public or use unit tests

Always test your examples with `cargo test --doc`!

