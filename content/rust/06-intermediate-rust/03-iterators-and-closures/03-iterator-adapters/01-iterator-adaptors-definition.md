## Iterator Adaptors Definition

What are iterator adaptors? What are their three defining characteristics?

---

Iterator adaptors are methods that transform iterators into new iterators. They are the building blocks of functional-style data processing in Rust.

**Three defining characteristics:**

1. **Lazy evaluation** - Don't execute until consumed
2. **Composable** - Can chain multiple adaptors together
3. **Zero-cost** - Compile down to efficient loops with no overhead

**Key insight:**
```rust
let pipeline = data.iter()
    .map(|x| x * 2)      // Creates structure
    .filter(|x| x > 10); // Creates structure
// Nothing executes yet!

let result: Vec<_> = pipeline.collect(); // NOW it executes
```

Adaptors create nested iterator types that themselves implement Iterator. Each adaptor wraps the previous iterator, building a pipeline factory that only runs when consumed.

The mental model: Think of adaptors as building a pipeline specification, not executing operations.

