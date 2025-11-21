## Iterator Trait Associated Type

Why does the Iterator trait use an associated type `Item` instead of a generic parameter? What's the difference?

---

The Iterator trait uses an associated type because each iterator type should produce exactly one item type.

**With associated type (actual design):**
```rust
pub trait Iterator {
    type Item;  // Associated type
    fn next(&mut self) -> Option<Self::Item>;
}

// Implementation
impl Iterator for MyIter {
    type Item = i32;  // This iterator yields i32s
    fn next(&mut self) -> Option<i32> { ... }
}
```

**Hypothetical generic version (why it's worse):**
```rust
// Hypothetical - NOT how it's designed
pub trait Iterator<T> {
    fn next(&mut self) -> Option<T>;
}

// Would allow multiple implementations
impl Iterator<i32> for MyIter { ... }
impl Iterator<String> for MyIter { ... }  // Ambiguous!
```

**Why associated type is better:**

1. **One output type per iterator:** An iterator should yield one type of item, not multiple
2. **No ambiguity:** `MyIter` has exactly one `Item` type
3. **Cleaner syntax:** Use `impl Iterator` instead of `impl Iterator<i32>`
4. **Type inference:** Compiler knows what type comes out

**Usage comparison:**
```rust
// With associated type (actual)
fn process(iter: impl Iterator<Item = i32>) { ... }

// Would be with generic (hypothetical)
fn process(iter: impl Iterator<i32>) { ... }
```

**The rule:** Use associated types when there's a clear one-to-one relationship. Use generics when you need flexibility in the number of implementations.

For Iterator, each iterator type has exactly one meaningful item type, making associated types the right choice.

