## Constants Scope

Where can constants be declared in Rust?

---

Constants can be declared in any scope, including global scope. They're accessible within their scope.

```rust
const GLOBAL_MAX: u32 = 100;  // Global constant

fn example() {
    const LOCAL_MAX: u32 = 50;  // Function-scoped constant
}
```

