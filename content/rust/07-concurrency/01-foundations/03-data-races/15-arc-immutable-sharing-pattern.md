## Arc Immutable Sharing Pattern

Why is sharing data with Arc<Vec<T>> across threads safe from data races?

---

Arc provides shared ownership with atomic reference counting, and the data inside is immutable (without additional primitives). Multiple threads can read the Vec simultaneously because all accesses are reads - no writes means no data race. Arc is Send + Sync, allowing it to cross thread boundaries. The type system prevents mutation without Mutex or other synchronization, guaranteeing all accesses are read-only.

