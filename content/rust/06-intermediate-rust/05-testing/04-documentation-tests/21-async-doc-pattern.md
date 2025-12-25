## Doc Test Async Code Pattern

How do you write documentation tests for async functions?

---

Use hidden runtime setup:

```rust
/// Fetches data from the API.
///
/// # Examples
///
/// ```
/// # tokio::runtime::Runtime::new().unwrap().block_on(async {
/// let data = fetch_user(42).await?;
/// assert_eq!(data.id, 42);
/// # Ok::<(), Box<dyn std::error::Error>>(())
/// # });
/// ```
pub async fn fetch_user(id: u32) -> Result<User, Error> {
    // Async implementation
}
```

Alternative with `no_run`:
```rust
/// # Examples
///
/// ```no_run
/// # async fn example() -> Result<(), Box<dyn std::error::Error>> {
/// let data = fetch_user(42).await?;
/// assert_eq!(data.id, 42);
/// # Ok(())
/// # }
/// ```
```

Hidden runtime allows async code to work in doc tests.

For complex async examples, `no_run` is often clearer.

