## Why Trait Bounds Are Necessary

Why can't you use operations like printing or comparison on generic types without trait bounds?

---

The compiler doesn't know what capabilities a generic type has. Without trait bounds, it can't guarantee the type supports the operations you want to use:

```rust
// ❌ Doesn't work
fn print_and_compare<T>(a: T, b: T) {
    println!("{}", a);     // Error: T might not be printable
    if a > b { }           // Error: T might not be comparable
}

// ✅ Works with bounds
fn print_and_compare<T: Display + PartialOrd>(a: T, b: T) {
    println!("{}", a);     // OK: T implements Display
    if a > b { }           // OK: T implements PartialOrd
}
```

