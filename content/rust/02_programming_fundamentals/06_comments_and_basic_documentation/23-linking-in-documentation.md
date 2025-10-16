## Linking in Documentation

How do you link to other items in documentation?

---

Use square brackets with backticks for intra-doc links.

```rust
/// Calculates using [`helper_function`].
/// See also [`std::collections::HashMap`].
fn calculate() { }
```

