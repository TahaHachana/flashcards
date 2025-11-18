## The dyn Keyword

What does the `dyn` keyword mean and why is it used with trait objects?

---

`dyn` stands for "dynamic dispatch" and explicitly marks trait objects:

```rust
Box<dyn Display>  // ✅ Correct (Rust 2018+)
Box<Display>      // ❌ Old syntax (no longer valid)
```

**Dynamic dispatch** means the method to call is determined at **runtime**, not compile time. The `dyn` keyword makes this explicit and distinguishes trait objects from other uses of traits.

