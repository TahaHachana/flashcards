## For Each Side Effects

What is `.for_each()` used for? How does it compare to a `for` loop?

---

`.for_each()` executes a closure on each element for side effects only.

**Signature:**
```rust
fn for_each<F>(self, f: F)
where F: FnMut(Self::Item)
```

**Basic usage:**
```rust
vec![1, 2, 3].iter().for_each(|x| println!("{}", x));

// Multiple operations
data.iter().for_each(|item| {
    log::info!("Processing: {:?}", item);
    process(item);
    update_metrics();
});
```

**Compared to for loop:**

**With `.for_each()` (method):**
```rust
data.iter()
    .filter(|x| x.is_valid())
    .for_each(|x| process(x));
```

**With `for` loop (statement):**
```rust
for x in data.iter().filter(|x| x.is_valid()) {
    process(x);
}
```

**Both have identical performance** - compiler generates same code.

**When to use `.for_each()`:**
- Part of iterator chain (method style)
- More functional/declarative style
- When it reads better

**When to use `for` loop:**
- Need early `break` or `continue`
- Complex control flow
- Multiple statements are clearer
- Traditional imperative style

**Differences:**

| Feature | .for_each() | for loop |
|---------|-------------|----------|
| Style | Method/functional | Statement/imperative |
| Early exit | Can't break | Can break/continue |
| Return value | None | Can return from loop |
| Chaining | Natural | Requires separate line |

**Example where for loop is better:**
```rust
// Can't do this with .for_each()
for item in data.iter() {
    if item.should_stop() {
        break;  // Early exit
    }
    process(item);
}
```

Use `.for_each()` when you truly want to perform an action on every element without early termination.

