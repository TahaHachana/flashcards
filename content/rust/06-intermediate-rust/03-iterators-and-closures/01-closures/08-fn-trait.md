## Fn Trait

What is the `Fn` trait, what does it mean for a closure, and when is it used?

---

`Fn` is the trait for closures that only read captured variables and can be called multiple times.

**Signature:**
```rust
pub trait Fn: FnMut {
    fn call(&self, args: Args) -> Self::Output;
}
```

**Key characteristics:**
- Takes `&self` (immutable borrow)
- Can be called unlimited times
- Implements all three traits: `Fn`, `FnMut`, and `FnOnce`
- Used for pure, non-mutating closures

**Example:**
```rust
fn takes_fn<F: Fn()>(f: F) {
    f(); // Can call as many times as needed
    f();
    f();
}

let message = String::from("Hello");
takes_fn(|| println!("{}", message)); // Only reads
```

Most restrictive capture, most flexible usage - can pass `Fn` closures anywhere.

