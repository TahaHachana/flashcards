## Closure Lifetime Requirements

What lifetime requirements do closures have for captured references? When does a closure need `'static` lifetime?

---

Closures that capture references must ensure those references live long enough.

**Normal usage (limited lifetime):**
```rust
fn process<F: Fn()>(f: F) {
    f();
} // Closure dropped here

let data = String::from("hello");
process(|| println!("{}", data)); // Borrows data
```

**Requires `'static` lifetime when:**

1. **Stored in structs or collections:**
```rust
struct Handler {
    callback: Box<dyn Fn() + 'static>,
}
```

2. **Passed to threads:**
```rust
thread::spawn(move || {
    // Must be 'static
})
```

3. **Returned from functions:**
```rust
fn make_closure() -> impl Fn() + 'static {
    // Must own all captured data
}
```

**Solution for `'static`:** Use `move` to give ownership:
```rust
let data = String::from("hello");
let closure = move || println!("{}", data);
// closure now has 'static lifetime
```

Without owned data, closures can't outlive their captured references.

