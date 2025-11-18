## Mutable Trait Objects

How do you use mutable trait objects?

---

Use `&mut dyn Trait` or `Box<dyn Trait>` (Box owns, so can mutate):

```rust
trait Modifiable {
    fn modify(&mut self);
}

struct Counter {
    count: u32,
}

impl Modifiable for Counter {
    fn modify(&mut self) {
        self.count += 1;
    }
}

fn modify_it(obj: &mut dyn Modifiable) {
    obj.modify();
}

fn main() {
    let mut counter = Counter { count: 0 };
    modify_it(&mut counter);
    
    // Or with Box
    let mut boxed: Box<dyn Modifiable> = Box::new(Counter { count: 0 });
    boxed.modify();  // Can call &mut self methods
}
```

