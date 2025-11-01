## When to Flatten vs Categorize

How do you decide between a flat API (everything at root) vs a categorized API (organized in modules)?

---

**Flatten to root when**:
- Small library (< 20 public items)
- Items don't conflict in naming
- All items are equally important/common
- Simplicity is highest priority

**Categorize when**:
- Large library (many items)
- Clear feature boundaries
- Some items are advanced/rarely used
- Want to avoid naming conflicts
- Organization aids understanding

**Decision factors**:

**Library size**:
- Small → Flatten
- Large → Categorize

**Item relationships**:
- Unrelated → Flatten individually
- Related groups → Categorize by group

**User level**:
- All beginners → Flatten essentials
- Mixed experience → Progressive disclosure (hybrid)

**Common pattern**: Start flat, add categories as library grows.

