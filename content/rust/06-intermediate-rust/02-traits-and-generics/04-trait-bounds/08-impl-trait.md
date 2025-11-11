## impl Trait Syntax

What is the `impl Trait` syntax and how does it differ from traditional trait bounds?

---

`impl Trait` is a shorthand for simple trait bounds:

```rust
// Traditional
fn process<T: Display>(value: T) { }

// impl Trait (shorter)
fn process(value: impl Display) { }
```

**Differences**:

- `impl Trait`: Simpler but you can't specify the concrete type
- Traditional generic: Can use turbofish syntax `function::<u8>(value)`

They're almost equivalent for simple cases, but `impl Trait` has limitations with return types.

