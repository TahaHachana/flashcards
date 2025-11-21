## Returning Closures

Why do you need `Box` or `impl Trait` to return closures from functions? Show both approaches.

---

Closures have unknown size at compile time because each closure is a unique type. Functions must know return type sizes, so you need indirection or `impl Trait`.

**Approach 1: Using `impl Trait`** (preferred, modern):
```rust
fn make_adder(n: i32) -> impl Fn(i32) -> i32 {
    move |x| x + n
}
```

**Approach 2: Using `Box<dyn Trait>`** (heap allocation):
```rust
fn make_adder(n: i32) -> Box<dyn Fn(i32) -> i32> {
    Box::new(move |x| x + n)
}
```

**Why this is needed:**
- Each closure has a unique, anonymous type
- The compiler needs to know the size of return types
- `impl Trait` or `Box` provides a fixed-size representation

The `move` keyword is typically required to ensure captured values are owned by the closure.

