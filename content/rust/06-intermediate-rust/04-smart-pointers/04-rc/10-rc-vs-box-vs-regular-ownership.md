## Rc vs Box vs Regular Ownership

Compare `Rc`, `Box`, and regular ownership across key features. When would you choose each?

---

| Feature | Ownership | Box | Rc |
|---------|-----------|-----|-----|
| **Owners** | One | One | Multiple |
| **Overhead** | None | None | Counter updates |
| **Mutability** | Via `mut` | Via `mut` | Needs `RefCell` |
| **Thread-safe** | Yes | Yes | No (use `Arc`) |
| **Use case** | Default | Heap allocation | Shared ownership |

**Decision guide:**
```
Need shared ownership?
  ├─ No → Use regular ownership or Box
  │       ├─ Need heap? → Box
  │       └─ Stack okay? → Regular ownership
  └─ Yes → Need thread safety?
      ├─ No → Use Rc
      └─ Yes → Use Arc
```

**Examples:**
```rust
// Regular ownership: single owner, stack
let data = String::from("hello");

// Box: single owner, heap
let data = Box::new(LargeData);

// Rc: multiple owners, single-threaded
let data = Rc::new(String::from("shared"));
let data2 = Rc::clone(&data);
```

