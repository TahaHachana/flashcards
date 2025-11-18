## What Are Trait Objects?

What is a trait object and what does it represent?

---

A trait object is a pointer to a value that implements a specific trait, but the exact concrete type is hidden (erased). Instead of knowing "this is a String", you know "this is *something* that implements Display."

```rust
let animal: Box<dyn Animal> = Box::new(Dog);
// We know it implements Animal
// We don't know it's a Dog (type is erased)
```

**Key**: You know what it can do (trait methods), but not what it is (concrete type).

