## Trait Dependency Hierarchy

What are the dependency relationships between `Ord`, `PartialOrd`, `Eq`, and `PartialEq`?

---

```
Ord
 ├── PartialOrd (required)
 └── Eq (required)
      └── PartialEq (required)
```

To derive `Ord`, you must also derive `PartialOrd`, `Eq`, and `PartialEq`:

```rust
#[derive(PartialEq, Eq, PartialOrd, Ord)]
struct Priority { value: u32 }
```

Order matters for readability (though compiler doesn't care).

