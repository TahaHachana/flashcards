## What Are Generic Types?

What are generic types and why do they exist in Rust?

---

Generic types allow you to write code that works with multiple types without rewriting the same logic for each type. Instead of writing separate functions for `i32`, `String`, `Vec`, etc., you write one generic function that works with any type `T`.

```rust
// Without generics - repetitive
fn return_i32(x: i32) -> i32 { x }
fn return_str(x: &str) -> &str { x }

// With generics - works for any type
fn return_item<T>(x: T) -> T { x }
```

**Purpose**: Code reuse, type safety, zero runtime cost.

