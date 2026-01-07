## Thread Safety Type System

How does the type system ensure thread safety when spawning threads?

---

thread::spawn requires the closure to be FnOnce + Send + 'static. Send ensures captured data can be safely transferred to another thread. 'static ensures no borrowed data with shorter lifetimes (prevents dangling references). The return type T must be Send to be transferred back via join. These compile-time checks prevent data races and use-after-free across thread boundaries. If your types don't satisfy these bounds, the code won't compile.

