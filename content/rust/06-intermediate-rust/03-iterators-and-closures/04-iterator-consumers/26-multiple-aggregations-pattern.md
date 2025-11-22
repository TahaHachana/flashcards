## Multiple Aggregations Pattern

Show how to compute multiple aggregations in a single pass through an iterator using fold.

---

Use fold with a tuple or struct to compute multiple values in one iteration.

**Pattern 1: Tuple accumulator**
```rust
let numbers = vec![1, 2, 3, 4, 5];

let (sum, product, count) = numbers.iter()
    .fold((0, 1, 0), |(sum, prod, count), &x| {
        (sum + x, prod * x, count + 1)
    });

let average = sum / count;
println!("Sum: {}, Product: {}, Count: {}, Avg: {}", 
    sum, product, count, average);
```

**Pattern 2: Struct accumulator**
```rust
#[derive(Debug, Default)]
struct Statistics {
    count: usize,
    sum: i32,
    sum_squared: i32,
    min: i32,
    max: i32,
}

let stats = numbers.iter().fold(
    Statistics {
        min: i32::MAX,
        max: i32::MIN,
        ..Default::default()
    },
    |mut acc, &x| {
        acc.count += 1;
        acc.sum += x;
        acc.sum_squared += x * x;
        acc.min = acc.min.min(x);
        acc.max = acc.max.max(x);
        acc
    }
);

let mean = stats.sum as f64 / stats.count as f64;
let variance = (stats.sum_squared as f64 / stats.count as f64) - mean * mean;
```

**Pattern 3: Multiple conditions**
```rust
let (positives, negatives, zeros) = numbers.iter()
    .fold((0, 0, 0), |(pos, neg, zero), &x| {
        match x {
            x if x > 0 => (pos + 1, neg, zero),
            x if x < 0 => (pos, neg + 1, zero),
            _ => (pos, neg, zero + 1),
        }
    });
```

**Pattern 4: Complex business logic**
```rust
#[derive(Default)]
struct TransactionSummary {
    total_amount: f64,
    transaction_count: usize,
    high_value_count: usize,
    fees_collected: f64,
}

let summary = transactions.iter().fold(
    TransactionSummary::default(),
    |mut acc, tx| {
        acc.total_amount += tx.amount;
        acc.transaction_count += 1;
        if tx.amount > 1000.0 {
            acc.high_value_count += 1;
        }
        acc.fees_collected += tx.fee;
        acc
    }
);
```

**Why single pass matters:**
```rust
// Bad - four passes through data
let sum: i32 = data.iter().sum();
let count = data.iter().count();
let max = data.iter().max();
let min = data.iter().min();

// Good - one pass
let (sum, count, max, min) = data.iter().fold(
    (0, 0, i32::MIN, i32::MAX),
    |(sum, count, max, min), &x| {
        (sum + x, count + 1, max.max(x), min.min(x))
    }
);
```

**Performance benefit:** O(n) vs O(4n) - significant for large datasets.

Single-pass aggregation with fold is idiomatic and efficient Rust.

