## Method Call Syntax Sugar

How does Rust's automatic referencing and dereferencing work with method calls?

---

Rust automatically adds `&`, `&mut`, or `*` to make method calls work:

```rust
let mut rect = Rectangle::new(10.0, 20.0);

// These are equivalent:
rect.area();
(&rect).area();

// These are equivalent:
rect.scale(2.0);
(&mut rect).scale(2.0);
```

This works with smart pointers too:
```rust
let boxed = Box::new(Rectangle::new(5.0, 10.0));
boxed.area();  // Rust auto-dereferences Box
```

This "method call syntax sugar" makes code cleaner and more ergonomic.

