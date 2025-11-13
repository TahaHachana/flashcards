## Generic Structs

How do you define and use a generic struct?

---

Declare generic parameters after the struct name:

```rust
struct Container<T> {
    value: T,
}

fn main() {
    let int_container = Container { value: 5 };
    let string_container = Container { 
        value: String::from("hello") 
    };
    let vec_container = Container { 
        value: vec![1, 2, 3] 
    };
}
```

The type `T` is determined when you create an instance. Each instance can hold a different type.

