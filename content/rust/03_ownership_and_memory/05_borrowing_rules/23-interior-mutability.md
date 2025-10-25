## Interior Mutability

What is interior mutability?

---

Mutation through shared references using types like RefCell. Uses runtime checking instead of compile-time. Wrong usage causes panic, not compile error.

```rust
let data = RefCell::new(5);
let r = data.borrow_mut();  // Runtime checked
```

