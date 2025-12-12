## Complete Decision Matrix

Provide a step-by-step decision tree for choosing the right smart pointer combination.

---

```
Step 1: Need heap allocation?
├─ Yes, for large data → Box<T>
├─ Yes, for recursive type → Box<T>
├─ Yes, for trait object → Box<dyn Trait>
└─ Also need sharing? → Continue to Step 2

Step 2: Need multiple owners?
├─ No → Box<T> or regular ownership
└─ Yes → Continue to Step 3

Step 3: Single-threaded or multi-threaded?
├─ Single-threaded → Rc<T>
├─ Multi-threaded → Arc<T>
└─ Continue to Step 4 if mutation needed

Step 4: Need mutability?
├─ No → Stop at Rc<T> or Arc<T>
└─ Yes → Continue to Step 5

Step 5: Choose interior mutability type
├─ Single-threaded?
│   ├─ Copy type → Rc<Cell<T>>
│   └─ Any type → Rc<RefCell<T>>
│
└─ Multi-threaded?
    ├─ Many reads, few writes → Arc<RwLock<T>>
    └─ General case → Arc<Mutex<T>>
```

**Quick reference:**
- Shared, immutable (single-thread) → `Rc<T>`
- Shared, mutable (single-thread) → `Rc<RefCell<T>>`
- Shared, immutable (multi-thread) → `Arc<T>`
- Shared, mutable (multi-thread) → `Arc<Mutex<T>>`
- Shared, read-heavy (multi-thread) → `Arc<RwLock<T>>`

