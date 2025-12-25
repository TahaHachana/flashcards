## Trait Requirements for assert_eq!

What traits must a type implement to use it with `assert_eq!` and why?

---

Types must implement:

1. **PartialEq**: To compare values for equality
2. **Debug**: To format error messages showing the values

Error without traits:
```rust
struct CustomType { value: i32 }

#[test]
fn broken() {
    let a = CustomType { value: 5 };
    let b = CustomType { value: 5 };
    assert_eq!(a, b);  // Error: traits not implemented
}
```

Solution:
```rust
#[derive(Debug, PartialEq)]
struct CustomType { value: i32 }

#[test]
fn works() {
    let a = CustomType { value: 5 };
    let b = CustomType { value: 5 };
    assert_eq!(a, b);  // Works!
}
```

