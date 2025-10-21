## Scope-Based Cleanup

When does drop run?

---

When the owning variable's scope ends. This is RAII (Resource Acquisition Is Initialization) - resources are tied to object lifetimes.

```rust
{
    let s = String::from("hello");
}  // s's scope ends, drop is called
```

