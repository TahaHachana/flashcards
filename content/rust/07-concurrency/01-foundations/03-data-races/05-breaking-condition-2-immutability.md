## Breaking Condition 2 Immutability

How does Rust allow breaking the second condition of data races (at least one write)?

---

Rust allows multiple threads to share immutable data using Arc<T>. Since all accesses are reads (no writes), there's no data race even though multiple threads access the same memory. The type system ensures you can't mutate data through an Arc without additional synchronization. Multiple readers are always safe - it's the writers that cause data races.

