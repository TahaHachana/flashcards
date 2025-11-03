## Pattern 3 Method Patterns Self Reference

What are the key characteristics of method patterns that return references to `self` or data owned by `self`?

---

Methods with `&self` or `&mut self` as receiver that return references with lifetime tied to `self`'s lifetime. Often no explicit lifetime annotations needed due to elision. Used for: getters/accessors, builder/fluent APIs (returning `&mut Self`), and iterator-like methods. Mental shortcut: "Method returns part of self" → implicit lifetime connection.

