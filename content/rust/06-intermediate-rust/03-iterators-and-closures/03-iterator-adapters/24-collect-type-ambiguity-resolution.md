## Collect Type Ambiguity Resolution

Why does `.collect()` often need type annotations? Show all three ways to provide them.

---

`.collect()` is generic over the collection type, requiring hints about what to build.

**The problem:**
```rust
let result = vec![1, 2, 3].iter()
    .map(|&x| x * 2)
    .collect();  // ❌ ERROR: type annotations needed
```

**Why:** `.collect()` can build many types:
```rust
fn collect<B: FromIterator<Self::Item>>(self) -> B
// B could be Vec, HashSet, HashMap, String, etc.
```

**Solution 1: Variable type annotation**
```rust
let result: Vec<i32> = vec![1, 2, 3].iter()
    .map(|&x| x * 2)
    .collect();
```

**Solution 2: Turbofish syntax `::<Type>`**
```rust
let result = vec![1, 2, 3].iter()
    .map(|&x| x * 2)
    .collect::<Vec<i32>>();
```

**Solution 3: Context from usage**
```rust
fn process_vec(v: Vec<i32>) { }

process_vec(
    vec![1, 2, 3].iter()
        .map(|&x| x * 2)
        .collect()  // ✓ Type inferred from function parameter
);
```

**Can collect into many types:**
```rust
// Vector
let vec: Vec<i32> = iter.collect();

// HashSet
let set: HashSet<i32> = iter.collect();

// HashMap (from iterator of pairs)
let map: HashMap<String, i32> = pairs_iter.collect();

// String (from chars)
let string: String = chars_iter.collect();

// Result<Vec<T>, E> (from iterator of Results)
let result: Result<Vec<_>, _> = result_iter.collect();
```

**Partial inference with `_`:**
```rust
// Specify outer type, infer inner
let result = iter.collect::<Vec<_>>();

// Specify collection but not error type
let result: Result<Vec<_>, _> = iter.collect();
```

**Pro tip:** Turbofish often reads better mid-chain:
```rust
data.iter()
    .filter(|x| x.is_valid())
    .map(|x| x.process())
    .collect::<Vec<_>>()  // Clear what type is being built
```

The compiler needs help because `collect()` is extremely flexible - it's a feature, not a bug!

