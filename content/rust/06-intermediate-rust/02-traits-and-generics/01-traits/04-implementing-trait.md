## Implementing a Trait

What is the syntax for implementing a trait called `Animal` for a type called `Dog`?

---

```rust
impl Animal for Dog {
    // Implement required methods here
    fn make_sound(&self) {
        println!("Woof!");
    }
}
```

The syntax is: `impl TraitName for TypeName { /* method implementations */ }`

