## Why Thread Spawn Requires Send

Why does thread::spawn require the closure and captured data to be Send + 'static?

---

Send is required because the closure is moved to a new thread - it must be safe to transfer ownership across thread boundaries. The 'static bound is required because the spawned thread can outlive the scope that created it, so it can't hold references to data that might be dropped. These bounds ensure the thread can safely own and access its data throughout its lifetime.

