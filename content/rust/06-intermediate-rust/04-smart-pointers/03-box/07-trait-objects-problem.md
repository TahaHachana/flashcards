## Trait Objects Problem

Why can't you return a trait directly from a function? What error occurs?

---

Different types implementing the same trait can have different sizes, so the compiler doesn't know how much space to allocate for the return value.

**The problem:**
```rust
trait Animal {
    fn speak(&self);
}

struct Dog;  // Some size
impl Animal for Dog {
    fn speak(&self) { println!("Woof!"); }
}

struct Cat;  // Different size
impl Animal for Cat {
    fn speak(&self) { println!("Meow!"); }
}

// ❌ This doesn't work
fn get_animal() -> Animal {
    Dog  // Error: trait objects have unknown size
}
```

**Compiler error:**
```
error[E0746]: return type cannot have an unboxed trait object
   --> doesn't have a size known at compile-time
```

**Why:** The compiler doesn't know if the function will return `Dog`, `Cat`, or something else. These types can have different sizes.

