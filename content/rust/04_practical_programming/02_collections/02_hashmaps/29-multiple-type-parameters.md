## Multiple Type Parameters

Can HashMap keys and values be different types? Give an example.

---

Yes! K and V are independent type parameters. Common patterns:
```rust
// String keys, integer values
HashMap<String, i32>

// Integer keys, vector values  
HashMap<i32, Vec<String>>

// Tuple keys, custom type values
HashMap<(i32, i32), Player>
```

