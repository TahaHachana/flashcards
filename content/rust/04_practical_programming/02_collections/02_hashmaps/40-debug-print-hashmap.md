## Debug Print HashMap

How do you print a HashMap for debugging and what's the output format?

---

Use `{:?}` with Debug trait:
```rust
let mut map = HashMap::new();
map.insert("a", 1);
map.insert("b", 2);
println!("{:?}", map);
```

Output (order varies): `{"b": 2, "a": 1}` or `{"a": 1, "b": 2}`

Order is unpredictable because HashMap is unordered.

