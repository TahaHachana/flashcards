## Why Smart Pointers for Trait Objects

Why do trait objects require smart pointers (or references)? Provide an example.

---

Trait objects have unknown size at compile time because different types implementing the trait have different sizes.

**Problem:**
```rust
trait Animal { fn speak(&self); }
// Error: trait objects don't have a known size
// let animal: Animal = Dog;
```

**Solution with Box:**
```rust
trait Animal { fn speak(&self); }

struct Dog;
impl Animal for Dog {
    fn speak(&self) { println!("Woof!"); }
}

fn get_animal() -> Box<dyn Animal> {
    Box::new(Dog)  // Type erased behind pointer
}
```

Smart pointers work because:
- The pointer itself has a known size
- The actual object is on the heap
- Runtime polymorphism (dynamic dispatch) is achieved through the vtable

This enables returning different types through the same interface.

