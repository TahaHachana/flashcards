## Option As Iterator

How does `Option<T>` behave as an iterator?

---

`Option<T>` implements `IntoIterator`, yielding 0 or 1 element:

```rust
// Some yields one element
for value in Some(5) {
    println!("{}", value);  // Prints 5 once
}

// None yields zero elements
for value in None {
    println!("{}", value);  // Never executes
}
```

This is useful with iterator combinators and allows Options to work seamlessly in iterator chains.

