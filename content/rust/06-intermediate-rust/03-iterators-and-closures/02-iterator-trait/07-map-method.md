## Map Method

What does the `.map()` iterator method do? Show how it transforms elements.

---

`.map()` transforms each element by applying a closure, returning a new iterator.

**Signature:**
```rust
fn map<B, F>(self, f: F) -> Map<Self, F>
where
    F: FnMut(Self::Item) -> B
```

**Usage:**
```rust
let numbers = vec![1, 2, 3, 4, 5];

let doubled: Vec<i32> = numbers.iter()
    .map(|x| x * 2)
    .collect();
// [2, 4, 6, 8, 10]

let strings: Vec<String> = numbers.iter()
    .map(|n| format!("Number: {}", n))
    .collect();
// ["Number: 1", "Number: 2", ...]
```

**Key characteristics:**
- Lazy adapter - doesn't execute until consumed
- One-to-one transformation (each input → one output)
- Can change type (i32 → String, etc.)
- Closure can capture environment

**Common pattern:**
```rust
vec.iter()
    .map(|&x| x * 2)  // Note: often need to dereference
    .collect()
```

