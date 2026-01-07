## Memory Safety Guarantee

How does move semantics prevent use-after-free in concurrent code?

---

Once data is moved into a thread, the parent can't access it - the compiler prevents this at compile time. This eliminates use-after-free: the parent can't drop data while the thread uses it, and can't access data after the thread takes ownership. Only one owner exists at a time. Combined with Send/Sync checks, move semantics provides compile-time memory safety guarantees in concurrent code.

