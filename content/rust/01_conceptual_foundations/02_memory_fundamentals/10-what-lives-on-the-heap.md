## What Lives on the Heap

What types of data live on the heap?

---

Dynamically-sized data (String, Vec<T>, HashMap<K,V>), data that needs to outlive a function's scope, data whose size isn't known at compile time, and large data structures to avoid stack overflow.

