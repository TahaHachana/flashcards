## Basic Trait Object Syntax

What are the three main ways to create trait objects?

---

```rust
// 1. Boxed (owned, heap-allocated)
let obj: Box<dyn Trait> = Box::new(value);

// 2. Reference (borrowed)
let obj: &dyn Trait = &value;

// 3. Mutable reference
let obj: &mut dyn Trait = &mut value;
```

**Most common**: `Box<dyn Trait>` for owned trait objects that can be stored in collections or returned from functions.

