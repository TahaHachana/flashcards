## Where Clauses

What are where clauses and when should you use them instead of inline trait bounds?

---

Where clauses place trait bounds after the function signature for better readability:

```rust
// Inline (harder to read)
fn function<T: Debug + Clone, U: Display + PartialEq>(t: T, u: U) { }

// Where clause (cleaner)
fn function<T, U>(t: T, u: U)
where
    T: Debug + Clone,
    U: Display + PartialEq,
{
    // function body
}
```

**Use where clauses when**:

- Multiple type parameters with bounds
- Complex bounds (more than 2 traits)
- Better readability is needed

