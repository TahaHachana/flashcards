## Filter Map vs Filter Plus Map

When should you use `.filter_map()` instead of `.filter().map()`? Show the performance difference.

---

Use `.filter_map()` when filtering and mapping can be combined into one operation returning `Option`.

**Less efficient - separate operations:**
```rust
let numbers: Vec<i32> = strings.iter()
    .filter(|s| s.parse::<i32>().is_ok())  // Parse once
    .map(|s| s.parse::<i32>().unwrap())    // Parse again!
    .collect();
```

**More efficient - combined operation:**
```rust
let numbers: Vec<i32> = strings.iter()
    .filter_map(|s| s.parse::<i32>().ok())  // Parse once!
    .collect();
```

**Why filter_map is better:**

**1. Single evaluation:**
```rust
// filter + map: evaluates twice
.filter(|x| expensive_check_returns_bool(x))
.map(|x| expensive_transform(x))

// filter_map: evaluates once
.filter_map(|x| expensive_combined_operation(x))
```

**2. Natural with Option/Result:**
```rust
// Awkward
vec_of_options.iter()
    .filter(|opt| opt.is_some())
    .map(|opt| opt.unwrap())

// Natural
vec_of_options.iter()
    .filter_map(|opt| *opt)
```

**3. Pattern matching integration:**
```rust
enum Status { Active(u32), Inactive, Pending(u32) }

// Elegant with filter_map
items.into_iter()
    .filter_map(|item| match item.status {
        Status::Active(id) => Some(id),
        Status::Pending(id) => Some(id),
        Status::Inactive => None,
    })
    .collect()

// Awkward with filter + map
items.iter()
    .filter(|item| matches!(item.status, Status::Active(_) | Status::Pending(_)))
    .map(|item| match item.status {
        Status::Active(id) | Status::Pending(id) => id,
        _ => unreachable!(),
    })
```

**When to use filter + map:**
- Filtering and mapping are logically separate
- Filter is very cheap, map is very expensive
- Better readability for simple cases

**When to use filter_map:**
- Operation naturally returns Option
- Checking and extracting are related
- Avoiding double evaluation
- Working with Option/Result chains

**Performance:** filter_map can be significantly faster when the operation is expensive or when working with large datasets.

