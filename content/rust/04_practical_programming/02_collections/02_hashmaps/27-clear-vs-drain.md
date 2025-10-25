## Clear vs Drain

What's the difference between `.clear()` and `.drain()` for HashMap?

---

`.clear()`: Removes all entries, keeps allocated capacity
```rust
map.clear(); // Now empty but capacity unchanged
```

`.drain()`: Removes and returns an iterator over all entries
```rust
for (k, v) in map.drain() {
    println!("{}: {}", k, v);
}
// map is now empty
```

