## Gotcha Method Returning Non-Self Reference

Why might elision not work correctly for this method, and what's the fix?

```rust
impl<'a> Processor<'a> {
    fn process(&self, input: &str) -> &str {
        // Process and return part of input, not self
    }
}
```

---

Rule 3 assumes methods return references from `self`, assigning `self`'s lifetime to the output. When the method actually returns from `input`, you need explicit annotations:
```rust
impl<'a> Processor<'a> {
    fn process<'b>(&self, input: &'b str) -> &'b str {
        // Return explicitly tied to input, not self
    }
}
```
This clarifies the output comes from `input`, not `self`.

