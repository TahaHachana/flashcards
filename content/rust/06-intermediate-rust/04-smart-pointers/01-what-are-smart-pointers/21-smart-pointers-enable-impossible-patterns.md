## Smart Pointers Enable Impossible Patterns

What patterns does Rust's ownership system make difficult or impossible without smart pointers? Provide examples.

---

Without smart pointers, these patterns are difficult or impossible:

**1. Shared Ownership (impossible with just `&T`):**
```rust
// Can't have multiple owners with references
// Smart pointer solution: Rc<T> or Arc<T>
let data = Rc::new(vec![1, 2, 3]);
let owner1 = Rc::clone(&data);
let owner2 = Rc::clone(&data);
```

**2. Recursive Types (impossible without indirection):**
```rust
// Can't define: infinite size
// Smart pointer solution: Box<T>
struct Node {
    next: Option<Box<Node>>,
}
```

**3. Interior Mutability (impossible with just ownership):**
```rust
// Can't mutate through & normally
// Smart pointer solution: RefCell<T>
let cell = RefCell::new(5);
fn modify(x: &RefCell<i32>) {
    *x.borrow_mut() = 10;  // Mutate through &
}
```

**4. Returning Different Types (impossible without type erasure):**
```rust
// Can't return different types
// Smart pointer solution: Box<dyn Trait>
fn get_animal(dog: bool) -> Box<dyn Animal> {
    if dog { Box::new(Dog) } else { Box::new(Cat) }
}
```

Smart pointers make these patterns safe and ergonomic.

