## Basic Implementation Syntax

Write the syntax to implement a trait called `Flyable` with a method `fly()` for a type called `Bird`.

---

```rust
impl Flyable for Bird {
    fn fly(&self) {
        println!("The bird is flying!");
    }
}
```

The syntax is: `impl TraitName for TypeName { /* method implementations */ }`

