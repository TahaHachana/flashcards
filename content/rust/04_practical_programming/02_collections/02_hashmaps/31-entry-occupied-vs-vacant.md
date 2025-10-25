## Entry Occupied vs Vacant

Explain the Entry enum returned by `.entry()` and its two variants.

---

```rust
enum Entry<K, V> {
    Occupied(OccupiedEntry<K, V>),  // Key exists
    Vacant(VacantEntry<K, V>),      // Key absent
}
```

Occupied: Contains existing key-value pair
Vacant: Represents empty slot for this key

Methods like `.or_insert()` handle both cases automatically.

