## The Newtype Pattern

What is the newtype pattern and when do you use it?

---

The newtype pattern wraps an external type in a tuple struct to create a new type, allowing you to implement external traits on it.

**Use case**: When you want to implement an external trait on an external type (which violates the orphan rule).

```rust
// Want Display for Vec<i32>, but can't due to orphan rule

// Wrap it in your own type
struct MyVec(Vec<i32>);

// Now you can implement Display!
impl Display for MyVec {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "{:?}", self.0)
    }
}
```

