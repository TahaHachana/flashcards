## Doc Test Verification Strategy

What should you verify in documentation test examples?

---

Verify key behaviors explicitly:

```rust
/// Creates a new user.
///
/// # Examples
///
/// ```
/// let user = User::new("Alice", 30);
///
/// // Verify construction
/// assert_eq!(user.name(), "Alice");
/// assert_eq!(user.age(), 30);
///
/// // Verify derived state
/// assert!(user.is_adult());
/// assert!(user.is_valid());
///
/// // Verify behavior
/// assert!(user.can_vote());
/// ```
```

What to verify:
- Input was properly stored
- Computed properties are correct
- State is valid
- Methods work as expected
- Edge cases handled

Don't just construct objects - show they work correctly!

Each `assert_eq!` documents expected behavior.

