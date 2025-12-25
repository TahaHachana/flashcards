## Send Sync Propagation

If you have `struct Container<T> { data: Vec<T> }`, when is Container Send and when is it Sync?

---

Container is Send when T is Send, because Vec<T> is Send when T is Send. Container is Sync when T is Sync, because Vec<T> is Sync when T is Sync. The traits propagate through composition: if any field lacks a trait, the containing type lacks it. If T is Rc<i32> (not Send/Sync), then Container is also not Send/Sync.

