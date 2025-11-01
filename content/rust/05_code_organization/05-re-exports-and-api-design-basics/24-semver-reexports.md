## Semver and Re-exports

How do re-exports relate to semantic versioning (semver)?

---

**Re-exports are part of your public API contract**, so they affect semver.

**Non-breaking changes** (patch/minor):
- ✅ Adding new re-exports
- ✅ Adding `#[deprecated]` to existing re-exports
- ✅ Adding new items to existing modules

**Breaking changes** (major):
- ❌ Removing re-exports (items no longer accessible)
- ❌ Moving items without maintaining old paths
- ❌ Changing re-export aliases

**Safe migration pattern**:
```rust
// Version 1.5 - Add new path, deprecate old
pub use new_location::Item;

#[deprecated(since = "1.5.0", note = "Use crate::Item instead")]
pub use old_location::Item as OldItem;

// Version 2.0 - Remove deprecated path
```

**Key insight**: Users depend on re-exported paths. Treat them as carefully as any other public API.

