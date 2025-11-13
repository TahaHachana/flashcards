## Basic Generic Function Syntax

What is the syntax for declaring a generic function?

---

Generic parameters are declared in angle brackets `<>` immediately after the function name:

```rust
fn function_name<T>(parameter: T) -> T {
    // function body
}
```

Example:
```rust
fn identity<T>(value: T) -> T {
    value
}

fn main() {
    let num = identity(42);        // T is i32
    let text = identity("hello");  // T is &str
}
```

The `<T>` declares a generic type parameter that can be used in parameters and return types.

