## Type Conversion Method Naming

What are the Rust naming conventions for type conversion methods?

---

Three common prefixes:

1. **`to_*`** - Creates a new value, potentially expensive
```rust
fn to_string(&self) -> String { }
fn to_vec(&self) -> Vec<T> { }
```

2. **`into_*`** - Consumes self, converts ownership
```rust
fn into_bytes(self) -> Vec<u8> { }
fn into_iter(self) -> IntoIter<T> { }
```

3. **`as_*`** - Cheap reference-to-reference conversion
```rust
fn as_str(&self) -> &str { }
fn as_bytes(&self) -> &[u8] { }
```

The prefix signals the cost and ownership semantics to the caller.

