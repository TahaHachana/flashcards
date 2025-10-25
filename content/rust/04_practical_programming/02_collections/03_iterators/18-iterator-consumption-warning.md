## Iterator Consumption Warning

What does this compiler warning mean and how do you fix it?
"warning: unused `Map` that must be used; iterators are lazy"

---

You created an iterator chain but didn't consume it:
```rust
// ❌ Warning:
vec.iter().map(|x| x * 2);

// ✅ Fixed - consume with collect:
let result: Vec<i32> = vec.iter()
    .map(|x| x * 2)
    .collect();
```
Must call a consuming method like `.collect()`, `.for_each()`, etc.

