## Mutable Iteration

How do you modify all values in a HashMap using iteration?

---

```rust
for (key, value) in map.iter_mut() {
    *value *= 2;  // Dereference to modify
}
```
Or to modify only values:
```rust
for value in map.values_mut() {
    *value *= 2;
}
```

