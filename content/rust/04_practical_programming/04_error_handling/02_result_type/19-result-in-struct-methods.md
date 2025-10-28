## Result In Struct Methods

How do you design struct methods that can fail using Results?

---

Return `Result` from methods that can fail:

```rust
struct DataStore {
    data: Vec<i32>,
}

impl DataStore {
    fn get(&self, index: usize) -> Result<i32, String> {
        self.data
            .get(index)
            .copied()
            .ok_or_else(|| format!("Index {} out of bounds", index))
    }
    
    fn add(&mut self, value: i32) -> Result<(), String> {
        if value < 0 {
            return Err("Cannot add negative values".into());
        }
        self.data.push(value);
        Ok(())
    }
}
```

