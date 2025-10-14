## Match as Expression

Can match statements be used as expressions?

---

Yes. match evaluates to a value and can be assigned.

```rust
let result = match value {
    1 => "one",
    2 => "two",
    _ => "other",
};
```

