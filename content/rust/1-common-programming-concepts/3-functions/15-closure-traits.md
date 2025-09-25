## Closure Traits

What are the three closure traits, and when are they used?

---

* `Fn` – captures by reference, can be called multiple times.
* `FnMut` – captures mutably, can modify captured values.
* `FnOnce` – consumes captured values, can only be called once.

Example:

```rust
fn apply<F: Fn()>(f: F) { f(); }
```

