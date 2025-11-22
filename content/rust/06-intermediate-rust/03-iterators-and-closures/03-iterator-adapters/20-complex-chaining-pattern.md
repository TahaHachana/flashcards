## Complex Chaining Pattern

Show a complex multi-stage transformation pattern that demonstrates proper iterator chaining with multiple adaptors.

---

Complex transformation combining multiple stages:

```rust
let report: HashMap<String, Summary> = raw_data
    .iter()
    // Stage 1: Clean and validate
    .filter(|item| item.is_valid())
    .map(|item| item.normalize())
    
    // Stage 2: Group by category
    .fold(HashMap::new(), |mut groups, item| {
        groups.entry(item.category().to_string())
            .or_insert_with(Vec::new)
            .push(item);
        groups
    })
    
    // Stage 3: Convert to iterator of groups
    .into_iter()
    
    // Stage 4: Aggregate each group
    .map(|(category, items)| {
        let summary = items.iter()
            .fold(Summary::default(), |acc, item| {
                acc.update(item)
            });
        (category, summary)
    })
    
    // Stage 5: Filter and collect
    .filter(|(_, summary)| summary.count > MIN_THRESHOLD)
    .collect();
```

**Breakdown:**

1. **Filter invalid** - Remove bad data early
2. **Normalize** - Consistent format
3. **Group** - Fold into HashMap by category
4. **Convert** - Back to iterator for processing
5. **Aggregate** - Compute summaries per group
6. **Filter** - Remove insignificant groups
7. **Collect** - Final result

**Why this pattern works:**

- Each stage independent and testable
- Lazy evaluation until final collect
- Type transformations clear
- Can add `.inspect()` between stages for debugging
- Single pass through data where possible

**Alternative with intermediate collection:**
```rust
// When you need to reuse intermediate results
let normalized: Vec<_> = raw_data.iter()
    .filter(|item| item.is_valid())
    .map(|item| item.normalize())
    .collect();

// Now can use normalized multiple times
let summary1 = normalized.iter().map(...).collect();
let summary2 = normalized.iter().filter(...).collect();
```

Real-world pattern for data processing pipelines.

