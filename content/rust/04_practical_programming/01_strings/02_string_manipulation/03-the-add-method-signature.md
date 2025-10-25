## The Add Method Signature

What is the signature of the add method used by the + operator and what does each parameter mean?

---

```rust
fn add(self, s: &str) -> String
```
- First parameter: self (takes ownership of the left String)
- Second parameter: &str (borrows the right string)
- Returns: new String

This explains why the left operand is moved and the right is borrowed when using +.

