## Lazy Evaluation

What does it mean that iterators are "lazy" in Rust? Show an example demonstrating lazy evaluation.

---

Iterators are **lazy** - they don't perform any work until consumed. Adapter methods just build up a chain of operations without executing them.

**Example:**
```rust
let numbers = vec![1, 2, 3, 4, 5];

// This doesn't execute yet - just creates the chain
let doubled = numbers.iter().map(|x| {
    println!("Doubling {}", x);
    x * 2
});

println!("Iterator created"); // No "Doubling" messages yet!

// Now it executes as we consume
for num in doubled {
    println!("Got: {}", num);
}
```

**Output:**
```
Iterator created
Doubling 1
Got: 2
Doubling 2
Got: 4
...
```

**Why laziness matters:**
- Only processes items actually used
- No intermediate allocations
- Can work with infinite sequences
- Can short-circuit early with `.take()`, `.find()`
- Operations fuse into single pass at compile time

