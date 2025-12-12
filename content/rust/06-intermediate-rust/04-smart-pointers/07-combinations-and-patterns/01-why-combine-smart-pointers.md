## Why Combine Smart Pointers?

Why do we need to combine smart pointers? What different problems does each layer solve?

---

Smart pointers solve different, orthogonal problems:

**Ownership:**
- Single owner: `Box`
- Multiple owners: `Rc` (single-threaded) or `Arc` (multi-threaded)

**Thread safety:**
- Single-threaded: `Rc`, `RefCell`
- Multi-threaded: `Arc`, `Mutex`, `RwLock`

**Mutability:**
- Compile-time: `&mut T`
- Runtime (interior mutability): `RefCell`, `Mutex`, `RwLock`

**Example needs:**
```
Need: Multiple owners + Mutability + Single-threaded
├─ Multiple owners → Rc
└─ Mutability → RefCell
Result: Rc<RefCell<T>>

Need: Multiple owners + Mutability + Multi-threaded
├─ Multiple owners → Arc
└─ Thread-safe mutability → Mutex
Result: Arc<Mutex<T>>
```

Often you need multiple capabilities at once, which requires combining smart pointers. Each layer addresses one specific problem.

