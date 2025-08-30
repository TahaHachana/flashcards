# Arrays vs Collections

When would you use arrays vs other collections in Rust?

---

Use arrays when:
- You want data allocated on the stack
- You know the number of elements won't change
- You need a fixed-size collection
For dynamic collections, use `Vec<T>` instead.