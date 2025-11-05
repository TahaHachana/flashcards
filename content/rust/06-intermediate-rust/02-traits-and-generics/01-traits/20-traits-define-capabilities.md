## Traits Define Capabilities

How do traits represent capabilities rather than identity? Give an example.

---

Traits express what something can DO, not what it IS. Multiple unrelated types can share the same capabilities.

```rust
trait Flyable {
    fn fly(&self);
}

struct Bird;
struct Airplane;
struct Superhero;

// All three can fly, but they're completely different types
impl Flyable for Bird { /* ... */ }
impl Flyable for Airplane { /* ... */ }
impl Flyable for Superhero { /* ... */ }
```

The trait `Flyable` defines a capability (flying) that these distinct types share, without creating a hierarchy.

