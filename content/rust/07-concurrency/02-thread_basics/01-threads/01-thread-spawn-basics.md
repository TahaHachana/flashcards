## Thread Spawn Basics

What does thread::spawn do, and what does it return?

---

thread::spawn creates and immediately starts a new OS thread that executes the provided closure. It returns a JoinHandle<T> where T is the return type of the closure. The function doesn't block - the new thread and calling thread both continue executing concurrently. The JoinHandle is used to wait for the thread to complete and retrieve its result.

