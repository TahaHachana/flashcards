## Cell vs RefCell vs Mutex

Compare `Cell`, `RefCell`, and `Mutex` across key features. When do you use each?

---

| Feature | Cell | RefCell | Mutex |
|---------|------|---------|-------|
| **Interior mutability** | Yes | Yes | Yes |
| **Works with** | Copy types | Any type | Any type |
| **Borrow checking** | None | Runtime | Runtime |
| **Thread-safe** | No | No | Yes |
| **Methods** | `get()`, `set()` | `borrow()`, `borrow_mut()` | `lock()` |
| **Can panic** | No | Yes | No (deadlock) |
| **Overhead** | None | Small | Larger |

**Decision guide:**
```
Need interior mutability?
  │
  ├─ Single-threaded?
  │   ├─ Type is Copy? → Cell
  │   └─ Type is not Copy? → RefCell
  │
  └─ Multi-threaded? → Mutex (or RwLock)
```

**Examples:**
```rust
// Cell: for Copy types
let cell = Cell::new(5);
cell.set(10);

// RefCell: for any type (single-threaded)
let refcell = RefCell::new(vec![1, 2, 3]);
refcell.borrow_mut().push(4);

// Mutex: for any type (multi-threaded)
let mutex = Mutex::new(vec![1, 2, 3]);
mutex.lock().unwrap().push(4);
```

