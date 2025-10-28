## Question Mark Error Creates New Value

Does the `?` operator return the same error value or create a new one?

---

The `?` operator may create a new error value due to the `From::from()` conversion:

```rust
let value = some_operation()?;
// The error returned is From::from(original_error)
```

This means:
- If types match, it's typically passed through unchanged
- If conversion is needed, a new error value is created
- You cannot rely on error value identity/pointer equality across `?`

This is usually not a concern, but matters if you're doing advanced error handling with pointer comparisons or using error values as keys.

