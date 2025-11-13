## Multiple Generic Parameters

How do you use multiple generic type parameters?

---

Declare multiple parameters separated by commas:

```rust
struct Pair<T, U> {
    first: T,
    second: U,
}

fn process<T, U>(x: T, y: U) -> T {
    println!("Processing two types");
    x
}

fn main() {
    let pair = Pair { first: 1, second: "hello" };
    // T=i32, U=&str
    
    process(42, "world");
    // T=i32, U=&str
}
```

Each generic parameter can be a different type.

