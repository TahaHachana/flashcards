## Inline vs Where Clause Decision

When should you use inline trait bounds vs where clauses?

---

**Use inline bounds** for:

- Simple cases with one type parameter
- Single trait bound
- Short, readable signatures

```rust
fn simple<T: Debug>(value: T) { }
```

**Use where clauses** for:

- Multiple type parameters
- Multiple trait bounds per parameter
- Associated type constraints
- Better readability

```rust
fn complex<T, U>(t: T, u: U)
where
    T: Debug + Clone + Display,
    U: Iterator<Item = i32>,
{
    // Much more readable!
}
```

