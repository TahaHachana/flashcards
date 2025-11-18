## Trait Object Method Access

What methods can you call on a trait object?

---

You can **only** call methods defined in the trait, not type-specific methods:

```rust
struct Dog {
    name: String,
}

impl Animal for Dog {
    fn make_sound(&self) { println!("Woof!"); }
}

impl Dog {
    fn get_name(&self) -> &str { &self.name }
}

let animal: Box<dyn Animal> = Box::new(Dog {
    name: String::from("Rover"),
});

animal.make_sound();  // ✅ Works: in Animal trait
// animal.get_name();  // ❌ Error: not in Animal trait
```

Type-specific methods are inaccessible after type erasure.

