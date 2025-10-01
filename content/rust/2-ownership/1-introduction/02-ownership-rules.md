## Ownership Rules

What are the three ownership rules in Rust?

---

1. Each value has a single owner.  
2. Only one owner can exist at a time.  
3. When the owner goes out of scope, the value is dropped (resources cleaned up via the `Drop` trait).

