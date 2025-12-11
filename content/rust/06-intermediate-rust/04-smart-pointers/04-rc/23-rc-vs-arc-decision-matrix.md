## Rc vs Arc Decision Matrix

Create a decision matrix: when to use `Rc` vs `Arc` (or neither)?

---

```
Need shared ownership?
  │
  ├─ No → Don't use Rc or Arc
  │       Use regular ownership or Box
  │
  └─ Yes → Is data accessed from multiple threads?
      │
      ├─ No (single-threaded)
      │   │
      │   └─ Use Rc<T>
      │       ├─ Need mutation? → Rc<RefCell<T>>
      │       └─ Read-only? → Rc<T>
      │
      └─ Yes (multi-threaded)
          │
          └─ Use Arc<T>
              ├─ Need mutation? → Arc<Mutex<T>> or Arc<RwLock<T>>
              └─ Read-only? → Arc<T>
```

**Quick reference table:**

| Scenario | Choice | Reason |
|----------|--------|--------|
| Single owner | Regular ownership | Simplest, fastest |
| Single owner, heap | `Box<T>` | Heap allocation |
| Multiple owners, 1 thread | `Rc<T>` | Cheap shared ownership |
| Multiple owners, threads | `Arc<T>` | Thread-safe |
| Shared mutation, 1 thread | `Rc<RefCell<T>>` | Interior mutability |
| Shared mutation, threads | `Arc<Mutex<T>>` | Thread-safe mutation |

**Cost comparison:**
- Regular ownership: Zero overhead
- `Box`: Heap allocation only
- `Rc`: Heap + counter updates
- `Arc`: Heap + atomic counter updates (slowest)

