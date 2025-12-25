## Testing with Moved Values

What ownership issue can occur when testing functions that take ownership, and how do you solve it?

---

Problem: Can't use value after it's moved:
```rust
#[test]
fn broken() {
    let s = String::from("hello");
    takes_ownership(s);
    assert_eq!(s, "hello");  // Error: value moved
}
```

Solutions:

1. Use function that returns ownership:
```rust
#[test]
fn solution1() {
    let s = String::from("hello");
    let result = returns_ownership(s);
    assert_eq!(result, "hello");
}
```

2. Clone before moving:
```rust
#[test]
fn solution2() {
    let s = String::from("hello");
    takes_ownership(s.clone());
    assert_eq!(s, "hello");  // Original still valid
}
```

