## Connection to Lifetime Patterns

Which common lifetime patterns do the elision rules automatically implement?

---

- Rule 2 implements Pattern 1 (single input → output)
- Rule 3 implements Pattern 3 (method returning from self)
- Rules don't matter for Pattern 5 (no output references)

Patterns that need explicit annotations: Pattern 2 (multiple sources, same lifetime) and Pattern 4 (multiple independent lifetimes) where relationships are non-obvious.

