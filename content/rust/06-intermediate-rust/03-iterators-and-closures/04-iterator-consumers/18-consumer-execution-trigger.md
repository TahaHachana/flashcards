## Consumer Execution Trigger

Why are consumers called "execution triggers"? Show what happens without a consumer.

---

Consumers trigger execution because adaptors are lazy and do nothing until consumed.

**Without consumer - nothing happens:**
```rust
// BUG: No execution!
vec![1, 2, 3].iter().map(|x| {
    println!("Processing {}", x);  // NEVER PRINTS
    x * 2
});

// Compiler warning: "unused `Map` that must be used"
```

**What's created:**
```rust
// Just builds a type structure
let _unused = vec![1, 2, 3].iter()
    .filter(|&&x| x > 0)
    .map(|&x| x * 2);
// Type: Map<Filter<Iter<i32>>> - but .next() never called!
```

**Adding consumer - triggers execution:**
```rust
vec![1, 2, 3].iter()
    .map(|x| {
        println!("Processing {}", x);  // NOW PRINTS
        x * 2
    })
    .collect::<Vec<_>>();  // CONSUMER - makes it run!
```

**How consumers trigger execution:**

1. Consumer calls `.next()` on the iterator
2. That cascades through all adaptors
3. Each element flows through the entire pipeline
4. Continues until iterator exhausted

**Different consumers, same trigger:**
```rust
// All of these trigger execution:
iter.collect::<Vec<_>>();
iter.sum();
iter.for_each(|x| process(x));
iter.any(|x| x > 10);
iter.count();

// None of these trigger execution:
iter.filter(|x| x > 0)
iter.map(|x| x * 2)
iter.take(10)
```

**Mental model:**
- Adaptors = Recipe instructions (dormant)
- Consumers = Chef executing recipe (active)

Without a consumer, you've written a recipe but no one cooks the meal.

