## What Are Trait Bounds?

What is a trait bound and what is its purpose?

---

A trait bound is a constraint on a generic type parameter that specifies which traits the type must implement. It tells the compiler: "This generic type T can be any type, but only if it has these specific capabilities."

```rust
fn process<T: Debug>(value: T) {
    println!("{:?}", value);  // OK because T must implement Debug
}
```

**Purpose**: Enable operations on generic types with compile-time guarantees.

