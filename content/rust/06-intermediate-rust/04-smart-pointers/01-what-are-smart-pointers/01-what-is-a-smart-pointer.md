## What is a Smart Pointer?

What is a smart pointer in Rust, and what are its three key characteristics that distinguish it from regular references?

---

A smart pointer is a data structure that acts like a pointer but includes additional capabilities. The three key characteristics are:

1. **Ownership**: Smart pointers own the data they point to (unlike references which only borrow)
2. **Metadata**: They maintain additional information about the data (like reference counts, capacity, etc.)
3. **Deref Capability**: They implement the `Deref` trait, allowing use of the `*` operator

The "smart" aspect refers to these extra capabilities beyond what regular references provide.

