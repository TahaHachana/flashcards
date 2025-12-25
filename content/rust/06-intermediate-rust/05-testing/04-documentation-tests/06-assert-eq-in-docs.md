## assert_eq! in Documentation

Why is `assert_eq!` used everywhere in Rust documentation instead of `println!`?

---

`assert_eq!` is superior for documentation:

With `println!`:
```rust
/// ```
/// let result = compute(5);
/// println!("{}", result);  // What's expected?
/// ```
```
Problems:
- Requires Display/Debug
- Doesn't verify correctness
- Output unclear

With `assert_eq!`:
```rust
/// ```
/// let result = compute(5);
/// assert_eq!(result, 10);  // Clear: expects 10
/// ```
```
Benefits:
- No trait requirements
- Tests verify correctness
- Shows expected values clearly
- Self-documenting behavior

`assert_eq!` makes examples both documentation AND tests.

