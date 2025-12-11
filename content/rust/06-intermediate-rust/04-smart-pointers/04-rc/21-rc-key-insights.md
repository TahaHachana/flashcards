## Rc Key Insights

What are the seven key insights about `Rc<T>`?

---

**1. Rc enables shared ownership:** Multiple parts can own the same data

**2. Reference counting is automatic:** No manual tracking needed

**3. Cloning is cheap:** Just increments a counter (~2-3 CPU cycles)

**4. Single-threaded only:** Use `Arc` for threads (Rc lacks `Send`/`Sync`)

**5. Immutable by default:** Need `RefCell` for mutation (`Rc<RefCell<T>>`)

**6. Weak prevents cycles:** Use `Weak` for back-references to avoid leaks

**7. Zero count = cleanup:** Automatic when last owner drops

**Mental model:**
- `Rc` = "reference counter" = shared ownership contract
- Data stays alive as long as someone holds a copy
- Cheap to share (clone pointer), expensive to copy (clone data)
- Like garbage collection, but deterministic

**Bottom line:** Rc provides safe shared ownership in single-threaded contexts without the complexity of lifetimes or the expense of cloning.

