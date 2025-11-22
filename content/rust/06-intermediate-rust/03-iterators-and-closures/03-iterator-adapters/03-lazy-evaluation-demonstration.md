## Lazy Evaluation Demonstration

Demonstrate lazy evaluation with an example showing when operations actually execute.

---

Iterator adaptors build structures without executing:

```rust
let nums = vec![1, 2, 3, 4, 5];

// This creates types but executes NOTHING
let pipeline = nums.iter()
    .map(|x| {
        println!("Mapping {}", x);  // Won't print!
        x * 2
    })
    .filter(|x| {
        println!("Filtering {}", x); // Won't print!
        x > &4
    });

println!("Pipeline created"); // Prints first

// NOW execution happens, element by element
let result: Vec<_> = pipeline.collect();
```

**Output:**
```
Pipeline created
Mapping 1
Filtering 2
Mapping 2
Filtering 4
Mapping 3
Filtering 6
...
```

**What's created:**
```rust
Filter<Map<std::slice::Iter<i32>>>
```

**Why it matters:**
- Can work with infinite sequences
- Operations only on items actually consumed
- No intermediate allocations
- Can short-circuit early
- Perfect for large or expensive data

Laziness enables efficiency - only compute what you need.

