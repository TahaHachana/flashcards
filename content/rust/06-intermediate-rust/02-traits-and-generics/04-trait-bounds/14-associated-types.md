## Associated Type Constraints

How do you constrain associated types in trait bounds?

---

Use the associated type syntax in the where clause:

```rust
fn sum_iterator<I>(iter: I) -> i32
where
    I: Iterator<Item = i32>,
{
    iter.sum()
}
```

This constrains the iterator's `Item` type to be `i32`.

Another example:
```rust
fn process<T>(value: T)
where
    T: Iterator,
    T::Item: Display + Clone,
{
    // Iterator items must implement Display and Clone
}
```

