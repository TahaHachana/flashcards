## Rc Thread Safety

Why does the compiler prevent sending Rc<T> between threads, and what data race would occur if it didn't?

---

Rc uses non-atomic reference counting for performance. If two threads both had Rc pointers and dropped them simultaneously, both would try to decrement the reference count at the same time without synchronization, causing a data race on the count itself. This could lead to use-after-free or memory leaks. The compiler prevents this by making Rc not Send - it can't cross thread boundaries.

