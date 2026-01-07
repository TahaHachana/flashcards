## JoinHandle Type

What is JoinHandle<T>, and what is T?

---

JoinHandle<T> is the handle returned by thread::spawn that represents the spawned thread. T is the return type of the closure passed to spawn - it's what the thread produces when it completes. For example, thread::spawn(|| 42) returns JoinHandle<i32>. You use the handle to wait for the thread (join) and retrieve its return value.

