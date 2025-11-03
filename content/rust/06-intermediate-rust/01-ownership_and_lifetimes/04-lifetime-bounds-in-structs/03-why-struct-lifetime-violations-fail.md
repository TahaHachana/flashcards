## Why Struct Lifetime Violations Fail

Why won't this code compile?
```rust
let excerpt;
{
    let novel = String::from("Call me Ishmael...");
    excerpt = Excerpt { text: &novel };
}
println!("{}", excerpt.text);
```

---

`novel` dies at the inner scope's closing brace, but `excerpt` tries to live beyond that point and use the reference in the `println!`. This would create a dangling reference. The borrow checker prevents this by ensuring `excerpt` cannot outlive the data it references.

