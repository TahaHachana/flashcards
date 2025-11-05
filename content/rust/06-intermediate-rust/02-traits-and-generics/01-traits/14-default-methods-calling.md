## Default Methods Calling Other Methods

How do you call one trait method from another trait method's default implementation?

---

You must use `self` to call other methods. Direct function calls won't work.

❌ Wrong:
```rust
trait Helper {
    fn step_one(&self);
    fn do_both(&self) {
        step_one();  // Error: not found
    }
}
```

✅ Correct:
```rust
trait Helper {
    fn step_one(&self);
    fn do_both(&self) {
        self.step_one();  // Correct
    }
}
```

