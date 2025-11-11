## Trait Bounds Make Generics Useful

Why are trait bounds essential for making generic types useful?

---

Without trait bounds, generic functions can't do anything with their parameters:

```rust
// Useless - can't do ANYTHING with T
fn do_nothing<T>(value: T) {
    // Can't print, clone, compare, or use value at all!
}

// Useful - can perform operations
fn do_something<T: Display + Clone>(value: T) {
    println!("{}", value);     // Can print
    let copy = value.clone();  // Can clone
    // Now we can actually work with the value!
}
```

Trait bounds are what make generic programming practical by enabling operations on generic types.

