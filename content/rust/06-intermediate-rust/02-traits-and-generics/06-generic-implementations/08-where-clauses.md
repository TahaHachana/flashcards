## Where Clauses in Impl Blocks

When and how should you use where clauses in generic implementations?

---

Use where clauses for complex trait bounds to improve readability:

```rust
// Inline (harder to read)
impl<T: Display + Clone, U: Debug + PartialEq> Pair<T, U> {
    fn describe(&self) { /* ... */ }
}

// Where clause (cleaner)
impl<T, U> Pair<T, U>
where
    T: Display + Clone,
    U: Debug + PartialEq,
{
    fn describe(&self) {
        println!("First: {}", self.first);
        println!("Second: {:?}", self.second);
    }
}
```

**Use when**: Multiple type parameters, multiple bounds per parameter, or when clarity is important.

