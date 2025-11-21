## Closure Type Uniqueness Gotcha

Why does this code fail to compile, and how do you fix it?

```rust
fn takes_two<F>(first: F, second: F)
where F: Fn() -> i32
{
    println!("{} {}", first(), second());
}

let a = || 5;
let b = || 5;
takes_two(a, b); // ERROR!
```

---

**Problem:** Every closure has a unique type, even if they look identical. The function expects both parameters to have the same type `F`, but `a` and `b` are different types.

**Solution 1: Separate type parameters** (most common):
```rust
fn takes_two<F, G>(first: F, second: G)
where
    F: Fn() -> i32,
    G: Fn() -> i32,
{
    println!("{} {}", first(), second());
}
```

**Solution 2: Trait objects**:
```rust
fn takes_two(
    first: Box<dyn Fn() -> i32>,
    second: Box<dyn Fn() -> i32>
) {
    println!("{} {}", first(), second());
}
```

Closures are like anonymous struct types - each definition creates a new type.

