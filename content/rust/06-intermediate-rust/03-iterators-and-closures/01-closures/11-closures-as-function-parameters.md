## Closures as Function Parameters

How do you write a function that accepts a closure as a parameter? Show the syntax with generic bounds.

---

Use generic type parameters with Fn trait bounds:

```rust
fn apply_operation<F>(value: i32, operation: F) -> i32
where
    F: Fn(i32) -> i32,
{
    operation(value)
}

fn main() {
    let result = apply_operation(5, |x| x * 2);
    println!("{}", result); // 10
}
```

**Syntax breakdown:**
- `<F>` - Generic type parameter for the closure
- `F: Fn(i32) -> i32` - Trait bound specifying:
  - Closure takes an `i32` parameter
  - Returns an `i32`
  - Implements `Fn` (can be called multiple times)

Can use `FnOnce`, `FnMut`, or `Fn` depending on how many times you need to call the closure.

