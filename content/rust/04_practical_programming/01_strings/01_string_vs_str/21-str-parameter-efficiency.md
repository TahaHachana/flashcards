## &str Parameter Efficiency

Why is taking &str as a parameter more efficient than taking String?

---

```rust
fn process(text: &str) { }    // More efficient
fn process(text: String) { }   // Less efficient
```
&str doesn't require ownership transfer or allocation if the caller already has &str or a String reference. Taking String forces the caller to either move their String or clone it, potentially causing unnecessary allocations.

