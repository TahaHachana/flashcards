## Making Impossible States Unrepresentable

How do enums help make impossible states unrepresentable? Show a bad struct design and its enum solution.

---

**Bad design with struct** - allows invalid states:
```rust
struct User {
    username: String,
    email: Option<String>,
    verified: bool,  // Problem: verified=true but email=None!
}
```

**Good design with enum** - invalid states impossible:
```rust
enum User {
    Unverified {
        username: String,
    },
    Verified {
        username: String,
        email: String,  // Always present for verified users
    },
}
```

The type system **enforces** that verified users have emails. The compiler won't let you create an invalid state.

**Principle**: Use enums to model mutually exclusive states where each state has different associated data.

