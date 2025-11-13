## Generic Naming Conventions

What are the conventional names for generic type parameters?

---

**Conventional single letters**:
- `T` - First generic type (Type)
- `U` - Second generic type
- `V` - Third generic type
- `E` - Error type (in `Result<T, E>`)

**Descriptive names** for clarity:
- `Key`, `Value` - for key-value pairs
- `Item` - for collections
- `Input`, `Output` - for transformations

```rust
fn process<T, U>(first: T, second: U) -> T { first }
// or
fn convert<Input, Output>(value: Input) -> Output { /* ... */ }
```

Single letters are more common, but use descriptive names when it aids clarity.

