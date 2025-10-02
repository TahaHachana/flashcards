## Field Access And Mutability

How do you access and modify struct fields, and what are the mutability rules?

---

* Access fields with dot syntax: `user1.email`.
* To modify, the entire instance must be mutable.

```rust
let mut user1 = user1;
user1.email = String::from("new@example.com");
```

