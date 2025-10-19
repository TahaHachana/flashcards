## Scope and Drop Order

When are values dropped in nested scopes?

---

Values are dropped when their scope ends, from innermost to outermost. Inner scope values drop first, then outer scope values.

```rust
{
    let s = String::from("hello");
    {
        let inner = String::from("world");
    }  // inner dropped here
}  // s dropped here
```

