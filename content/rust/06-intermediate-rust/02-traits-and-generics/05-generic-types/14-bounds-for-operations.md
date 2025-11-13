## Generics Require Trait Bounds for Operations

Why can't you perform operations like comparison or printing on generic types without trait bounds?

---

The compiler doesn't know what operations are valid for an arbitrary type `T`:

```rust
// ❌ WRONG: Can't compare without bounds
fn compare<T>(a: T, b: T) -> bool {
    a > b  // Error: T might not implement PartialOrd
}

// ❌ WRONG: Can't print without bounds
fn display<T>(value: T) {
    println!("{}", value);  // Error: T might not implement Display
}

// ✅ CORRECT: Add trait bounds
fn compare<T: PartialOrd>(a: T, b: T) -> bool {
    a > b  // Works!
}
```

Trait bounds tell the compiler what operations are guaranteed to work.

