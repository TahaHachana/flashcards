## Which Traits Cannot Be Derived?

Why can't `Display` be derived, and what other traits cannot be derived?

---

**Display cannot be derived** because it requires human decision on how to format output for end users. The compiler can't guess your intended formatting.

**Other non-derivable traits**:
- `From`/`Into` - Requires custom conversion logic
- `Iterator` - Requires custom iteration logic
- Most custom traits - Too complex or context-dependent

These must be implemented manually with `impl` blocks.

