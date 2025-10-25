## Cannot Modify While Borrowing

Why does this fail and how do you fix it?
```rust
for (key, value) in &map {
    map.insert("new", 10);  // ERROR
}
```

---

The for loop borrows `map` immutably, so you can't modify it. 

**Fix**: Collect keys first, then modify:
```rust
let keys: Vec<_> = map.keys().cloned().collect();
for key in keys {
    map.insert("new", 10);  // OK now
}
```

