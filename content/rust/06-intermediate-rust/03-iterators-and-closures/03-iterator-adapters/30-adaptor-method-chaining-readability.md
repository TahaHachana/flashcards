## Adaptor Method Chaining Readability

What are best practices for formatting long iterator chains for readability?

---

Well-formatted chains make complex pipelines understandable.

**Bad - all on one line:**
```rust
let result = data.iter().filter(|x| x.is_valid()).map(|x| x.process()).filter(|x| x.score > 50).take(10).collect::<Vec<_>>();
```

**Good - one operation per line:**
```rust
let result: Vec<_> = data.iter()
    .filter(|x| x.is_valid())
    .map(|x| x.process())
    .filter(|x| x.score > 50)
    .take(10)
    .collect();
```

**With comments for complex operations:**
```rust
let report = transactions.iter()
    // Remove cancelled transactions
    .filter(|tx| tx.status != Status::Cancelled)
    
    // Normalize amounts to USD
    .map(|tx| tx.to_usd())
    
    // Group by date
    .fold(HashMap::new(), |mut map, tx| {
        map.entry(tx.date).or_insert_with(Vec::new).push(tx);
        map
    })
    
    // Calculate daily totals
    .into_iter()
    .map(|(date, txs)| {
        let total = txs.iter().map(|tx| tx.amount).sum();
        (date, total)
    })
    .collect();
```

**For very long closures - extract to functions:**
```rust
fn is_valid_transaction(tx: &Transaction) -> bool {
    tx.amount > 0.0 
        && tx.status != Status::Cancelled
        && tx.date <= today()
}

let filtered = transactions.iter()
    .filter(is_valid_transaction)
    .collect();
```

**Indentation for nested operations:**
```rust
let processed = data.iter()
    .map(|item| {
        let normalized = item.normalize();
        let enhanced = normalized.enhance();
        enhanced.finalize()
    })
    .collect();
```

**Grouping logical stages:**
```rust
let result = data.iter()
    // Stage 1: Validation
    .filter(|x| x.is_valid())
    .filter(|x| x.timestamp.is_recent())
    
    // Stage 2: Transformation
    .map(|x| x.normalize())
    .map(|x| x.enrich_with_metadata())
    
    // Stage 3: Aggregation
    .fold(Summary::default(), |acc, x| acc.update(x));
```

**Type annotations at the end:**
```rust
let ids: Vec<u64> = users.iter()
    .filter(|u| u.is_active)
    .map(|u| u.id)
    .collect();  // Type clear from variable annotation
```

**Guidelines:**
1. One operation per line
2. Align `.` at start of line
3. Group related operations with blank lines
4. Add comments for complex logic
5. Extract complex closures to functions
6. Put type annotation on variable or final collect()

Good formatting makes iterator chains self-documenting.

