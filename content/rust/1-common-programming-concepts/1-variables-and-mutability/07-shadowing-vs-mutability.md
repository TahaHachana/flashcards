## Shadowing Vs Mutability

How is shadowing different from using `mut`?

---

* `mut` changes the value of the **same** variable without creating a new binding.
* Shadowing creates a **new** variable, possibly with a different type, reusing the same name.

Key idea:
*Shadowing = new binding. Mutability = same binding.*

```rust
// Shadowing can change type:
let spaces = "   ";
let spaces = spaces.len(); // &str → usize

// Mutability cannot change type:
let mut spaces = "   ";
// spaces = spaces.len(); // ❌ type mismatch
```

