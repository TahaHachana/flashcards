## Best Practices Summary

Summarize the seven best practices for using smart pointers safely and effectively.

---

**1. Choose appropriately**
- Start simple (regular ownership)
- Add smart pointers only when needed
- Use simplest type that works

**2. Avoid reference cycles**
- Use `Weak` for back-references
- Monitor reference counts (`Rc::strong_count`)
- Document ownership relationships

**3. Handle runtime errors**
- Use `try_borrow`/`try_lock` when unsure
- Keep borrow/lock duration minimal
- Add proper error handling

**4. Prevent deadlocks**
- Consistent lock ordering (always lock in same order)
- Minimize lock duration (lock late, unlock early)
- Avoid nested locks
- Consider lock-free alternatives (channels)

**5. Monitor performance**
- Profile before optimizing
- Benchmark critical paths
- Reduce unnecessary smart pointers
- Batch operations

**6. Test thoroughly**
- Unit tests for basic functionality
- Stress tests for concurrency
- Memory leak detection (Valgrind)
- Deadlock detection

**7. Document intent**
```rust
/// Uses Arc<Mutex<T>> because:
/// - Shared across threads (Arc)
/// - Needs mutation (Mutex)
/// Lock ordering: Always acquire data_mutex before config_mutex
struct SharedState {
    data: Arc<Mutex<Data>>,
}
```

**Bottom line:** Balance benefits (shared ownership, interior mutability) against costs (performance, complexity, potential runtime errors).

