## &str Lifetime Rules

Why does this code fail to compile?
```rust
let slice: &str;
{
    let s = String::from("hello");
    slice = &s[..];
}
println!("{}", slice);
```

---

The code fails because &str follows reference lifetime rules. The String s doesn't live long enough - it's dropped at the end of the inner scope, but slice tries to reference it outside that scope. This would create a dangling reference, so Rust prevents compilation.

