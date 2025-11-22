## Iterator Consumers Definition

What are iterator consumers? How do they differ from iterator adaptors?

---

Iterator consumers are terminal operations that consume an iterator and produce a final result, triggering execution of the entire pipeline.

**Key differences:**

```markdown
| Aspect | Adaptors | Consumers |
|--------|----------|-----------|
| Return type | Iterator | Concrete value |
| Execution | Lazy (deferred) | Eager (immediate) |
| Ownership | `self` → Iterator | `self` → Value |
| Chainable | Yes | No (terminal) |
| Examples | map, filter | collect, sum |
```

**Signatures comparison:**
```rust
// Adaptor - returns iterator
fn map<F>(self, f: F) -> Map<Self, F>

// Consumer - returns value
fn sum<S>(self) -> S
```

**Mental model:** If adaptors write a recipe, consumers execute it.

```rust
data.iter()
    .filter(predicate)  // Adaptor (lazy)
    .map(transform)     // Adaptor (lazy)
    .collect()          // CONSUMER - triggers execution!
```

Consumers are the "execution trigger" - nothing happens until you use one.

