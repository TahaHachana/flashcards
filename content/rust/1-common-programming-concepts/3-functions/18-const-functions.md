## Const Functions

What are `const fn`s in Rust, and how are they used?

---

* `const fn` can be evaluated at compile time in constant contexts.
* They can also be called at runtime.
* Useful for defining constants that need computation.

Example:

```rust
const fn square(x: i32) -> i32 { x * x }
const N: i32 = square(12);

fn main() {
    println!("N = {N}");
}
```

