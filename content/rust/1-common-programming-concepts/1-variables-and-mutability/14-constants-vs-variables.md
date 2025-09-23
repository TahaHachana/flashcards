## Constants vs Variables

Why might you use a `const` instead of an immutable `let` binding?

---

* `const` is evaluated at compile time.
* Can appear in global scope.
* Has no runtime overhead (inlined wherever used).
* Immutable `let` bindings are evaluated at runtime and have scope-based lifetimes.

