## Reduce vs Fold Difference

How does `.reduce()` differ from `.fold()`? When would you use each?

---

Both reduce iterators to single values, but differ in initial value handling.

**Fold - requires initial value:**
```rust
fn fold<B, F>(self, init: B, f: F) -> B
```

```rust
let sum = vec![1, 2, 3, 4].iter()
    .fold(0, |acc, &x| acc + x);
// 10
```

**Reduce - uses first element:**
```rust
fn reduce<F>(self, f: F) -> Option<Self::Item>
```

```rust
let max = vec![3, 7, 2, 9, 1].into_iter()
    .reduce(|a, b| a.max(b));
// Some(9)
```

**Key differences:**

| Aspect | fold | reduce |
|--------|------|--------|
| Initial value | Required | Uses first element |
| Return type | `B` | `Option<Item>` |
| Empty iterator | Returns init | Returns None |
| Type flexibility | Can change type | Same type |

**Empty iterator behavior:**
```rust
// fold with empty
let sum = Vec::<i32>::new().iter().fold(0, |acc, &x| acc + x);
// 0 (returns init)

// reduce with empty
let max = Vec::<i32>::new().into_iter().reduce(|a, b| a.max(b));
// None
```

**Use fold when:**
- Need specific initial value
- Accumulator type differs from item type
- Empty iterator should return meaningful default

**Use reduce when:**
- First element is natural starting point
- Same type for accumulator and items
- Empty iterator should be None

