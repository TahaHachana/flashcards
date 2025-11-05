## Most Common Derive Pattern

What is the most common derive pattern used for regular structs?

---

```rust
#[derive(Debug, Clone)]
struct MyStruct {
    // fields
}
```

**Debug** allows debugging with `{:?}`, and **Clone** provides explicit duplication. Almost every struct should have at least these two traits.

For simple data types, you might add more:
```rust
#[derive(Debug, Clone, PartialEq)]
```

