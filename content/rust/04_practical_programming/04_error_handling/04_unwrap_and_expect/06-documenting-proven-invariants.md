## Documenting Proven Invariants

How should you use `expect()` when you've proven an error is logically impossible?

---

Use `expect()` with a clear message explaining the invariant:

```rust
fn get_middle_element(vec: &Vec<i32>) -> i32 {
    let len = vec.len();
    *vec.get(len / 2)
        .expect("BUG: Middle element must exist for non-empty vec")
}

// Only called with non-empty vectors
fn process_data(data: Vec<i32>) {
    assert!(!data.is_empty(), "Data must not be empty");
    let middle = get_middle_element(&data);
}
```

**Key principles:**
- Always document **why** the unwrap is safe
- Use "BUG:" prefix to indicate this should never happen
- Explain the invariant or precondition
- Make it clear this is a programming error if it panics

Never use bare `unwrap()` without explanation in production.

