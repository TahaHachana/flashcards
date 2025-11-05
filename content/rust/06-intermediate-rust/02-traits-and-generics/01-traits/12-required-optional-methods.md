## Required vs Optional Methods

What's the difference between a required method and an optional method in a trait?

---

**Required method**: Only has a signature, no body. Implementers MUST provide the implementation.
```rust
trait MyTrait {
    fn required(&self);  // No body - must implement
}
```

**Optional method**: Has a default body. Implementers can use the default or override it.
```rust
trait MyTrait {
    fn optional(&self) {  // Has body - can override
        println!("Default");
    }
}
```

