## FnOnce Trait

What is the `FnOnce` trait, what does it mean for a closure, and when is it used?

---

`FnOnce` is the trait for closures that consume captured variables and can only be called once.

**Signature:**
```rust
pub trait FnOnce {
    fn call_once(self, args: Args) -> Self::Output;
}
```

**Key characteristics:**
- Takes `self` by value (consumes the closure)
- Can only be called once
- All closures implement this trait
- Used when closure moves/consumes captured values

**Example:**
```rust
fn takes_fnonce<F: FnOnce()>(f: F) {
    f(); // Can only call once
}

let s = String::from("hello");
takes_fnonce(|| drop(s)); // Consumes s
```

The name "once" indicates it takes ownership and can only execute once.

