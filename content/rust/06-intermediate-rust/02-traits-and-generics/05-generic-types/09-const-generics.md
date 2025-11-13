## Const Generics

What are const generics and what problem do they solve?

---

Const generics allow types to be generic over constant values, primarily used for array sizes:

```rust
struct ArrayWrapper<T, const N: usize> {
    array: [T; N],
}

fn main() {
    let small = ArrayWrapper { array: [1, 2, 3] };      // N=3
    let large = ArrayWrapper { array: [1, 2, 3, 4, 5] }; // N=5
}
```

**Problem solved**: Before const generics, you needed different structs for each array size. Now one generic struct works for any size.

The syntax `const N: usize` declares a compile-time constant generic parameter.

