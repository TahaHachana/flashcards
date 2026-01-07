## Thread Lifetime Requirements

Why do regular threads require 'static lifetime or ownership, and how do scoped threads avoid this?

---

Regular threads can outlive the scope that spawned them - they might run forever or until process exit. Therefore captured data must either be owned (moved) or have 'static lifetime. Scoped threads avoid this by guaranteeing all spawned threads complete before the scope ends, allowing safe borrowing of local data. The scope acts as a join point that ensures threads finish before borrowed data is dropped.

