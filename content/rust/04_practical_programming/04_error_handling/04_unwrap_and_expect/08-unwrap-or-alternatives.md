## Unwrap Or Alternatives

What are the safe alternatives to `unwrap()` for providing default values?

---

Use the `unwrap_or*` family of methods that don't panic:

**`unwrap_or(default)`** - Provide a default:
```rust
let value = result.unwrap_or(0);  // Returns 0 on Err
```

**`unwrap_or_else(fn)`** - Compute default lazily:
```rust
let value = result.unwrap_or_else(|err| {
    eprintln!("Error: {}", err);
    0
});
```

**`unwrap_or_default()`** - Use type's default:
```rust
let value = result.unwrap_or_default();  // 0 for numbers, "" for String
```

These are **always preferred** over `unwrap()` when you have a reasonable default value.

