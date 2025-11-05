## Trait Implementation and Ownership

How do the three forms of `self` in trait methods affect ownership?

---

Trait implementations must respect ownership rules:

```rust
trait Processor {
    fn process(self);        // Takes ownership (consumes)
    fn inspect(&self);       // Borrows immutably
    fn modify(&mut self);    // Borrows mutably
}

impl Processor for Data {
    fn process(self) {
        // self consumed, can't use after
    }
    fn inspect(&self) {
        // Can read, not modify
    }
    fn modify(&mut self) {
        // Can modify
    }
}
```

The method signature determines whether the value is borrowed or moved.

