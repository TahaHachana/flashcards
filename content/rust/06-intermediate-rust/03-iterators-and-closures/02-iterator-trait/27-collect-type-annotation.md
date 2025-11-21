## Collect Type Annotation

Why does `.collect()` often need type annotations? Show three ways to provide them.

---

`.collect()` is generic over the collection type, so the compiler often can't infer which collection you want.

**Problem:**
```rust
// ERROR: type annotations needed
let result = vec![1, 2, 3].iter()
    .map(|&x| x * 2)
    .collect();
// Compiler doesn't know: Vec? HashSet? LinkedList?
```

**Solution 1: Variable type annotation:**
```rust
let result: Vec<i32> = vec![1, 2, 3].iter()
    .map(|&x| x * 2)
    .collect();
```

**Solution 2: Turbofish syntax:**
```rust
let result = vec![1, 2, 3].iter()
    .map(|&x| x * 2)
    .collect::<Vec<i32>>();
```

**Solution 3: Context from usage:**
```rust
fn process_vec(v: Vec<i32>) { }

process_vec(
    vec![1, 2, 3].iter()
        .map(|&x| x * 2)
        .collect()  // Type inferred from function parameter
);
```

**Can collect into many types:**
```rust
let vec: Vec<i32> = iter.collect();
let set: HashSet<i32> = iter.collect();
let string: String = char_iter.collect();
let result: Result<Vec<_>, _> = result_iter.collect();
```

**Partial inference with underscore:**
```rust
// Infer inner type, specify outer
let result = iter.collect::<Vec<_>>();
```

The compiler needs help because `.collect()` implements `FromIterator` for many collection types.

