## FnMut Trait

What is the `FnMut` trait, what does it mean for a closure, and when is it used?

---

`FnMut` is the trait for closures that mutate captured variables and can be called multiple times.

**Signature:**
```rust
pub trait FnMut: FnOnce {
    fn call_mut(&mut self, args: Args) -> Self::Output;
}
```

**Key characteristics:**
- Takes `&mut self` (mutable borrow)
- Can be called multiple times
- Implements both `FnMut` and `FnOnce`
- Used when closure needs to modify environment

**Example:**
```rust
fn takes_fnmut<F: FnMut()>(mut f: F) {
    f(); // Can call multiple times
    f();
}

let mut count = 0;
takes_fnmut(|| count += 1); // Mutates count
```

The closure binding must also be `mut`: `let mut closure = || ...`

