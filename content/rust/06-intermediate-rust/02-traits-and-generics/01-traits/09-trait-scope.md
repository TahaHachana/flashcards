## Trait Scope Requirement

Why might calling a trait method fail even though a type implements that trait? What's the solution?

---

The trait must be in scope with a `use` statement. Even if a type implements a trait, you can't use the trait's methods unless the trait is imported.

Problem:
```rust
fn main() {
    let x = MyType;
    x.some_method();  // Error: method not found
}
```

Solution:
```rust
use my_crate::MyTrait;  // Bring trait into scope

fn main() {
    let x = MyType;
    x.some_method();  // Now works!
}
```

