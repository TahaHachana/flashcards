## Associated Functions in Traits

What is an associated function in a trait, and how does it differ from a method?

---

An associated function is a function defined in a trait that does NOT take any form of `self` as a parameter. It's called on the type itself, not on instances.

Example:
```rust
trait Factory {
    fn create() -> Self;  // Associated function (no self)
    fn modify(&self);     // Method (has self)
}

// Called as:
let instance = MyType::create();  // Type::function()
instance.modify();                // instance.method()
```

