## Quick Reference Table

Create a quick reference table for choosing smart pointer combinations based on common needs.

---

```markdown
| Need                  | Single-Threaded    | Multi-Threaded     |
|-----------------------|--------------------|--------------------|
| Shared, immutable     | Rc<T>              | Arc<T>             |
| Shared, mutable       | Rc<RefCell<T>>     | Arc<Mutex<T>>      |
| Shared, read-heavy    | Rc<RefCell<T>>     | Arc<RwLock<T>>     |
| Single owner, heap    | Box<T>             | Box<T>             |
| Trait object          | Box<dyn T>         | Box<dyn T + Send>  |
| Shared trait object   | Rc<dyn T>          | Arc<dyn T>         |
```

**Decision shortcuts:**

**Threading?**
- One thread → `Rc` family
- Multiple threads → `Arc` family

**Mutability?**
- No → Just `Rc` or `Arc`
- Yes (single-thread) → Add `RefCell`
- Yes (multi-thread) → Add `Mutex` or `RwLock`

**Read/write pattern?**
- Balanced or write-heavy → `Mutex`
- Read-heavy (90%+ reads) → `RwLock`

**Ownership?**
- Single owner → `Box`
- Multiple owners → `Rc` or `Arc`

**Remember:** Start simple, add complexity only when needed.

