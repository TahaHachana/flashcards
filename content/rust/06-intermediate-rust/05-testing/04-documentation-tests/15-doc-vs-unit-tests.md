## Doc Tests vs Unit Tests

When should you use documentation tests versus unit tests?

---

**Documentation tests:**
- Public API only
- User-facing examples
- Show how to use code
- Part of documentation
- Simple, clear examples

```rust
/// # Examples
/// ```
/// let result = add(2, 2);
/// assert_eq!(result, 4);
/// ```
pub fn add(a: i32, b: i32) -> i32 { a + b }
```

**Unit tests:**
- Can test private functions
- Internal verification
- Not shown to users
- Can be complex/messy
- Thorough edge case coverage

```rust
#[cfg(test)]
mod tests {
    #[test]
    fn test_internal_logic() {
        assert_eq!(internal_helper(5), 10);
    }
}
```

Use both: Doc tests for examples, unit tests for comprehensive coverage.

