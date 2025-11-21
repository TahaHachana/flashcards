## Collect Method

What does `.collect()` do? Why does it often need type annotations?

---

`.collect()` consumes an iterator and builds a collection from its elements.

**Signature:**
```rust
fn collect<B: FromIterator<Self::Item>>(self) -> B
```

`.collect()` is generic and can produce many types, so it often needs type hints:

**Type annotation methods:**

1. **Variable type:**
```rust
let vec: Vec<i32> = (1..5).collect();
```

2. **Turbofish syntax:**
```rust
let vec = (1..5).collect::<Vec<i32>>();
```

3. **Through context:**
```rust
fn takes_vec(v: Vec<i32>) { }
takes_vec((1..5).collect()); // Type inferred
```

**Can collect into many types:**
```rust
let vec: Vec<i32> = iter.collect();
let set: HashSet<i32> = iter.collect();
let string: String = chars.collect();
let result: Result<Vec<_>, _> = results.collect();
```

**Error without annotation:**
```rust
let result = vec.iter().map(|x| x * 2).collect();
// ERROR: type annotations needed
```

