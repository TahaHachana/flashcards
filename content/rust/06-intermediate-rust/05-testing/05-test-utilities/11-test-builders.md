## Test Data Builders

How do you implement the builder pattern for test data?

---

Create builders for flexible test data:

```rust
struct UserBuilder {
    name: String,
    age: u32,
    email: String,
}

impl UserBuilder {
    fn new() -> Self {
        // Sensible defaults
        UserBuilder {
            name: "TestUser".to_string(),
            age: 25,
            email: "test@example.com".to_string(),
        }
    }
    
    fn name(mut self, name: &str) -> Self {
        self.name = name.to_string();
        self
    }
    
    fn age(mut self, age: u32) -> Self {
        self.age = age;
        self
    }
    
    fn build(self) -> User {
        User::new(&self.name, self.age, &self.email)
    }
}

#[test]
fn test() {
    let user = UserBuilder::new()
        .name("Alice")
        .age(30)
        .build();
    assert_eq!(user.name(), "Alice");
}
```

Benefits: Readable, flexible, minimal setup required.

