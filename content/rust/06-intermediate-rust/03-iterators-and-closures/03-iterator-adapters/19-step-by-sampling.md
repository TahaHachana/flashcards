## Step By Sampling

What does `.step_by()` do? Show use cases for sampling data.

---

`.step_by(n)` creates an iterator that yields every nth element, skipping n-1 in between.

**Signature:**
```rust
fn step_by(self, step: usize) -> StepBy<Self>
```

**Every other element:**
```rust
let every_other: Vec<i32> = (0..10)
    .step_by(2)
    .collect();
// [0, 2, 4, 6, 8]
```

**Every third element:**
```rust
let every_third: Vec<i32> = data.iter()
    .step_by(3)
    .copied()
    .collect();
// Takes elements at indices 0, 3, 6, 9, ...
```

**Data sampling:**
```rust
// Sample every 100th measurement for overview
let samples: Vec<Measurement> = all_measurements.iter()
    .step_by(100)
    .cloned()
    .collect();
```

**Processing every Nth row:**
```rust
// Process every 5th row (e.g., for performance)
let selected: Vec<_> = rows.iter()
    .step_by(5)
    .map(|row| row.process())
    .collect();
```

**Downsampling video frames:**
```rust
// Keep every 3rd frame (reduce from 60fps to 20fps)
let downsampled: Vec<Frame> = frames.iter()
    .step_by(3)
    .cloned()
    .collect();
```

**Important notes:**
- Zero-indexed: first element (index 0) is always included
- `step_by(1)` means every element (no skipping)
- `step_by(2)` means every other element (skip 1)
- Panics if step is 0

**Pattern - odds vs evens:**
```rust
let evens = (0..10).step_by(2).collect::<Vec<_>>();
// [0, 2, 4, 6, 8]

let odds = (1..10).step_by(2).collect::<Vec<_>>();
// [1, 3, 5, 7, 9]
```

Useful for downsampling, performance optimization, and periodic processing.

