## Send Sync Trait Bounds

When writing generic functions or types that work with threads, what trait bounds should you typically add and why?

---

Add T: Send when the function will transfer ownership of T to another thread (move it into thread::spawn). Add T: Sync when multiple threads will share references to T. Often use T: Send + Sync together for types that need to be both moved and shared across threads. The 'static bound is also often needed because threads can outlive their parent scope.

