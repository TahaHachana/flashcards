## Safe Slicing by Character Position

Why is this safe_slice function necessary and what does it do?

---

```rust
fn safe_slice(s: &str, start: usize, end: usize) -> Option<&str> {
    let indices: Vec<_> = s.char_indices().map(|(i, _)| i).collect();
    
    if start >= indices.len() || end > indices.len() {
        return None;
    }
    
    let start_byte = indices[start];
    let end_byte = if end < indices.len() {
        indices[end]
    } else {
        s.len()
    };
    
    Some(&s[start_byte..end_byte])
}
```
Converts character positions to byte positions using char_indices(), ensuring slices are always at valid UTF-8 boundaries. Prevents panics from invalid slicing.

