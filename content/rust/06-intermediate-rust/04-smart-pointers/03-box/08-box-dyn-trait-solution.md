## Box<dyn Trait> Solution

How does `Box<dyn Trait>` solve the trait object size problem? Provide a working example.

---

`Box<dyn Trait>` has a known size (pointer + vtable pointer) regardless of the actual type inside.

**Solution:**
```rust
trait Animal {
    fn speak(&self);
}

struct Dog;
impl Animal for Dog {
    fn speak(&self) { println!("Woof!"); }
}

struct Cat;
impl Animal for Cat {
    fn speak(&self) { println!("Meow!"); }
}

// ✅ This works!
fn get_animal(is_dog: bool) -> Box<dyn Animal> {
    if is_dog {
        Box::new(Dog)
    } else {
        Box::new(Cat)
    }
}

fn main() {
    let animal = get_animal(true);
    animal.speak();  // Woof!
}
```

**How it works:**
- `Box<dyn Animal>` has known size (16 bytes: pointer + vtable)
- Actual type (`Dog` or `Cat`) is on heap
- Dynamic dispatch uses vtable to call correct method at runtime

