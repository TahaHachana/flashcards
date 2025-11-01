## Best Practices Summary

What are the key best practices for re-exports and API design in Rust?

---

**Best practices**:

**1. Two-layer approach**:
- Internal layer: optimize for maintainability
- Public layer: optimize for usability

**2. User-first thinking**:
- Design for how users want to work
- Don't expose implementation details

**3. Progressive disclosure**:
- Common items at root or in obvious places
- Advanced items in deeper modules
- Prelude for maximum convenience

**4. Stability**:
- Maintain re-exports for backward compatibility
- Use `#[deprecated]` for migrations
- Follow semver rules

**5. Logical organization**:
- Group by functionality, not implementation
- Put items where users expect them
- Use clear, consistent naming

**6. Balance**:
- Flat for small libraries
- Categorized for large libraries
- Hybrid for medium libraries

**Golden rule**: Optimize your internal organization for the team maintaining it, and your public API for the developers using it. Re-exports bridge these two needs.

