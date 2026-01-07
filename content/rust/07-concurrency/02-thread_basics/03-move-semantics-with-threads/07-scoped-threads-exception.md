## Scoped Threads Exception

How do scoped threads (thread::scope) allow borrowing without move?

---

thread::scope guarantees all spawned threads complete before the scope ends. This bounds the threads' lifetimes - they can't outlive the borrowed data. The scope acts as a join point, automatically joining all threads when it exits. Since threads are guaranteed to finish before data is dropped, borrowing is safe. The lifetime constraint is enforced at compile time through the scope's lifetime parameter.

