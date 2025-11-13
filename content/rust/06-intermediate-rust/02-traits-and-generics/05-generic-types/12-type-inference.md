## Generic Type Inference

When do you need to explicitly specify generic types, and how do you do it?

---

**When compiler can't infer**: Functions that return generics without taking them as parameters.

```rust
fn create_default<T: Default>() -> T {
    T::default()
}

fn main() {
    // ❌ Error: can't infer type
    let value = create_default();
    
    // ✅ Type annotation
    let value: i32 = create_default();
    
    // ✅ Turbofish syntax
    let value = create_default::<i32>();
}
```

**Turbofish syntax**: `::<Type>` after function name specifies the generic type explicitly.

