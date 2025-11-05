## Traits and Zero-Cost Abstractions

What does "zero-cost abstraction" mean in the context of traits?

---

Zero-cost abstraction means that using traits has no runtime performance penalty. Trait methods are statically dispatched by default, meaning:

1. The compiler knows exactly which implementation to call at compile time
2. No virtual function table lookups or indirection
3. Can be inlined by the optimizer
4. Same performance as calling the method directly

You get the abstraction benefit without paying a performance cost.

