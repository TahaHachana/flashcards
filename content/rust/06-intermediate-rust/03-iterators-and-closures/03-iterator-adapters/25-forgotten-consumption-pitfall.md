## Forgotten Consumption Pitfall

What happens when you forget to consume an iterator chain? Why doesn't the code execute?

---

Iterator adaptors are lazy - without a consumer, they build structures but execute nothing.

**The bug:**
```rust
vec![1, 2, 3].iter().map(|x| {
    println!("Processing {}", x);  // Never prints!
    x * 2
});
// Nothing happens!
```

**Why it fails:**
```rust
// This creates a Map<Iter<i32>> struct
let _unused = vec![1, 2, 3].iter().map(|x| x * 2);
// Map struct is created but .next() never called
// Compiler may warn: "unused `Map` that must be used"
```

**The fix - add a consumer:**

**Option 1: `.collect()`**
```rust
vec![1, 2, 3].iter()
    .map(|x| {
        println!("Processing {}", x);  // Now prints!
        x * 2
    })
    .collect::<Vec<_>>();
```

**Option 2: `.for_each()`**
```rust
vec![1, 2, 3].iter().for_each(|x| {
    println!("Processing {}", x);  // Prints!
});
```

**Option 3: `for` loop**
```rust
for x in vec![1, 2, 3].iter().map(|x| x * 2) {
    println!("{}", x);  // Prints!
}
```

**Other consumers that trigger execution:**
- `.sum()`, `.product()`
- `.count()`, `.last()`, `.nth()`
- `.find()`, `.any()`, `.all()`
- `.fold()`, `.reduce()`

**Compiler warning:**
```
warning: unused `Map` that must be used
  |
  | vec![1, 2, 3].iter().map(|x| x * 2);
  | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  |
  = note: iterators are lazy and do nothing unless consumed
```

**Why this design:**
- Efficiency (don't compute what you don't need)
- Composability (build complex chains)
- Short-circuiting (stop early when possible)

**Mental model:** Adaptors write a recipe; consumers execute it. No consumer = no execution.

