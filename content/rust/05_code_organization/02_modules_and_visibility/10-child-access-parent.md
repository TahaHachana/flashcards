## Child Modules Can Access Parent Items

Can a child module access private items in its parent module? Why or why not?

---

**Yes**, child modules can always access parent items, regardless of visibility.

**Rationale**: A child module is "inside" its parent. Think of it like geography - if you're in a city, you're automatically in its province and country.

**Example**:
```rust
mod country {
    fn print_country(name: &str) {  // Private
        println!("Country: {}", name);
    }
    
    pub mod city {
        pub fn print_city(country: &str, city: &str) {
            super::print_country(country);  // Can access parent's private function
            println!("City: {}", city);
        }
    }
}
```

**Key point**: Privacy only restricts access from outside, not from children within.

