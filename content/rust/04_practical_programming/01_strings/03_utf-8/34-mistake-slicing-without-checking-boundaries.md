## Mistake - Slicing Without Checking Boundaries

Why does this panic and how do you slice safely?
```rust
let s = String::from("你好");
let slice = &s[0..1];
```

---

```rust
// ❌ Panics: not on character boundary
let slice = &s[0..1];

// ✅ Correct: slice at valid boundaries
let slice = &s[0..3];  // "你" (complete 3-byte char)

// Or use char_indices to find boundaries
for (i, _) in s.char_indices() {
    println!("Valid boundary: {}", i);
}
```
Must slice at character boundaries, not arbitrary byte positions.

