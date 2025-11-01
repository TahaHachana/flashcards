## Complete Path Example with Super and Crate

Show how to use both absolute (`crate::`) and relative (`super::`) paths to access the same function.

---

```rust
mod country {
    fn print_country(name: &str) {
        println!("Country: {}", name);
    }
    
    pub mod province {
        fn print_province(name: &str) {
            println!("Province: {}", name);
        }
        
        pub mod city {
            pub fn print_all(country: &str, province: &str) {
                // Absolute path from crate root
                crate::country::print_country(country);
                
                // Relative path - up two levels
                super::super::print_country(country);
                
                // Both call the same function!
                
                // Up one level for province
                super::print_province(province);
            }
        }
    }
}
```

**Key insight**: Child modules can access parent functions either way—choose based on clarity.

