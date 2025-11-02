## Lifetime Subtyping Relationship

What does the lifetime bound `'b: 'a` mean?

---

`'b: 'a` means "`'b` outlives `'a`" or "`'b` lives at least as long as `'a`". This is a lifetime bound that establishes a hierarchy. If `'a` ⊇ `'b` in scope terms, then `'b` is a subset of `'a`, so `'b: 'a` in bound syntax. Rust can often infer these relationships automatically.

