## RefCell Key Insights

What are the seven key insights about `RefCell<T>`?

---

**1. Interior mutability trades compile-time for runtime:** RefCell moves borrow checking from compilation to execution

**2. Same rules, different timing:** The borrowing rules are identical, just enforced at runtime

**3. Use sparingly:** Prefer regular mut when possible, RefCell when necessary

**4. Common with Rc:** `Rc<RefCell<T>>` is the standard pattern for shared mutable state (single-threaded)

**5. Not thread-safe:** Use `Mutex` for multi-threaded interior mutability

**6. Can panic:** Unlike compile-time checks, RefCell can panic at runtime if rules violated

**7. Prefer try_ methods:** Use `.try_borrow()` and `.try_borrow_mut()` when unsure to avoid panics

**Mental model:**
```
Regular Rust: Compiler enforces rules → Safe, strict
RefCell: You enforce rules → Flexible, can panic
```

**When to use:**
- API requires `&self` but need mutation
- Building mock objects for tests
- Implementing caching
- Complex data structures (graphs/trees)

**Bottom line:** RefCell is a powerful tool for interior mutability. Use it when architecture demands mutation through immutable references, but prefer compile-time safety whenever possible.

