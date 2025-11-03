## When to Use Structs with Lifetimes

What are good and questionable use cases for structs with lifetime parameters?

---

Good: Parsing (hold slices of input), iterators (traverse borrowed data), views (temporary windows), configuration (references to shared config), zero-copy processing.

Questionable: Long-lived data structures (consider owned data), public APIs (lifetimes can be constraining), when cloning is cheap enough.

The key is whether borrowing provides meaningful benefits over owning.

