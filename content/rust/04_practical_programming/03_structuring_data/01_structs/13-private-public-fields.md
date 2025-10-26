## Private vs Public Struct Fields

What is the default visibility of struct fields in Rust, and how do you create a public API with controlled access?

---

**Default**: All fields are **private** to the module.

To create controlled access:
```rust
pub struct BankAccount {
    owner: String,      // private
    balance: f64,       // private
}

impl BankAccount {
    pub fn new(owner: String) -> Self {
        BankAccount { owner, balance: 0.0 }
    }
    
    pub fn balance(&self) -> f64 {
        self.balance
    }
    
    pub fn deposit(&mut self, amount: f64) {
        if amount > 0.0 {
            self.balance += amount;
        }
    }
}
```

Users can't directly access or modify private fields, ensuring data consistency through the public API.

