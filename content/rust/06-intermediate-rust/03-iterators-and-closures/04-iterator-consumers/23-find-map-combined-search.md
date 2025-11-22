## Find Map Combined Search

What does `.find_map()` do? When is it more efficient than `.find().map()`?

---

`.find_map()` combines finding and transforming into one operation, returning `Option`.

**Signature:**
```rust
fn find_map<B, F>(self, f: F) -> Option<B>
where F: FnMut(Self::Item) -> Option<B>
```

**How it works:**
- Closure returns `Some(value)` → found and transformed
- Closure returns `None` → keep searching

**Efficient - single evaluation:**
```rust
let result = data.iter()
    .find_map(|item| {
        if item.is_valid() {
            Some(item.expensive_transform())
        } else {
            None
        }
    });
```

**Less efficient - evaluates twice:**
```rust
let result = data.iter()
    .find(|item| item.is_valid())
    .map(|item| item.expensive_transform());
```

**Pattern matching in find_map:**
```rust
enum Status { Active(u32), Inactive, Pending(u32) }

let first_active_id = statuses.iter()
    .find_map(|status| match status {
        Status::Active(id) => Some(*id),
        Status::Pending(id) => Some(*id),
        Status::Inactive => None,
    });
```

**Parsing with early success:**
```rust
let first_valid_number = strings.iter()
    .find_map(|s| s.parse::<i32>().ok());
// Returns first successfully parsed number
```

**Database lookup:**
```rust
let user = user_ids.iter()
    .find_map(|id| database.get_user(id));
// Returns first found user
```

**Why it's better:**
1. **Single evaluation** - expensive operation runs only if condition met
2. **Short-circuits** - stops at first Some
3. **More expressive** - combines condition and extraction

**Use when:**
- Searching with transformation
- Operation is expensive
- Pattern matching with extraction
- Working with Option/Result chains

Equivalent to `.filter_map().next()` but more semantic.

