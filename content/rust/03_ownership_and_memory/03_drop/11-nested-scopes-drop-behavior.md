## Nested Scopes Drop Behavior

How does drop work with nested scopes?

---

Drop happens at each scope boundary. Inner scope values drop when inner scope ends, outer scope values drop when outer scope ends.

```rust
{
    let outer = String::from("outer");
    {
        let inner = String::from("inner");
    }  // inner dropped here
}  // outer dropped here
```

