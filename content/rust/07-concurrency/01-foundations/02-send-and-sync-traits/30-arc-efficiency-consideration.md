## Arc Efficiency Consideration

What is the performance cost of Arc compared to Rc, and when should you avoid using Arc unnecessarily?

---

Arc uses atomic operations for reference counting, which are slower than Rc's non-atomic operations due to memory ordering guarantees and potential cache coherency overhead. Use Arc only when you actually need to share data across threads. If your code is single-threaded, use Rc for better performance. Don't use Arc "just in case" you might need threading later - pay for thread safety only when you need it.

