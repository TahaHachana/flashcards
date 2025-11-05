## Conditional Trait Implementation

How do you implement a trait conditionally based on generic type parameters?

---

Use trait bounds on the generic parameter in the impl block:

```rust
struct Wrapper<T> {
    value: T,
}

// Only implement Display if T implements Display
impl<T: Display> Display for Wrapper<T> {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "Wrapped: {}", self.value)
    }
}

// This works:
let w = Wrapper { value: 42 };
println!("{}", w);  // i32 implements Display

// This doesn't:
let w = Wrapper { value: vec![1, 2] };
// println!("{}", w);  // Vec doesn't implement Display
```

