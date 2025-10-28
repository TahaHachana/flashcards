## Question Mark Best Practices

What are the best practices for using the `?` operator effectively?

---

**DO:**
- Use `?` for idiomatic error propagation
- Make function signatures return `Result` when using `?`
- Use `?` in tests for cleaner setup code
- Let `?` handle automatic error conversion via `From`

**DON'T:**
- Use `?` just to hide error handling without thinking
- Overuse `Box<dyn Error>` in libraries (loses type info)
- Forget that `?` returns early (cleanup before `?`)
- Mix `Option` and `Result` `?` without conversion

**REMEMBER:**
`?` makes error propagation ergonomic while maintaining Rust's explicit error handling philosophy.

