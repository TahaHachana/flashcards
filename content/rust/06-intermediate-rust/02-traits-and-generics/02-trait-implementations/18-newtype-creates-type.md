## Why Newtype Creates New Type

Why does wrapping an external type in a tuple struct allow you to bypass the orphan rule?

---

The tuple struct creates a **new type** that is local to your crate. Even though it contains an external type, the wrapper itself is yours.

```rust
struct MyVec(Vec<i32>);  // MyVec is YOUR type
```

Since `MyVec` is defined in your crate:
- You can implement external traits (like `Display`) for it
- The orphan rule is satisfied: either the trait OR the type is local

The wrapped `Vec<i32>` is just data inside your type.

