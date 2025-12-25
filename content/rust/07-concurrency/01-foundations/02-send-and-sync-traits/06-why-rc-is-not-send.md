## Why Rc Is Not Send

Why is Rc<T> not Send, and what problems would occur if it were?

---

Rc<T> uses non-atomic reference counting for performance. If two threads both had Rc pointers and dropped them simultaneously, they could both try to modify the reference count at the same time, causing a data race and potentially corrupting the count. This could lead to use-after-free or memory leaks. The compiler prevents this by making Rc not implement Send, so you can't move it between threads.

