## Position vs Find

What's the difference between `.position()` and `.find()`? When would you use each?

---

Both search for elements matching a predicate, but return different information.

**Find - returns the element:**
```rust
fn find<P>(self, predicate: P) -> Option<Self::Item>
```

```rust
let first_even = numbers.iter()
    .find(|&&x| x % 2 == 0);
// Some(&6) - returns reference to element
```

**Position - returns the index:**
```rust
fn position<P>(&mut self, predicate: P) -> Option<usize>
```

```rust
let position = numbers.iter()
    .position(|&x| x % 2 == 0);
// Some(3) - returns index where found
```

**Comparison:**

| Method | Returns | Use when |
|--------|---------|----------|
| `.find()` | `Option<Item>` | Need the value itself |
| `.position()` | `Option<usize>` | Need the index/location |

**Using position for indexing:**
```rust
if let Some(pos) = numbers.iter().position(|&x| x == target) {
    println!("Found at index {}", pos);
    let value = &numbers[pos];  // Can index with result
}
```

**Find for immediate use:**
```rust
if let Some(user) = users.iter().find(|u| u.id == target_id) {
    process_user(user);  // Have the actual user
}
```

**Both short-circuit** - stop at first match for efficiency.

Choose based on what you need: the element itself or its position.

