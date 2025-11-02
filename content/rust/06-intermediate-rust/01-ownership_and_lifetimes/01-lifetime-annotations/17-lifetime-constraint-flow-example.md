## Lifetime Constraint Flow Example

Why doesn't this compile?
```rust
let string1 = String::from("long");
let result;
{
    let string2 = String::from("short");
    result = longest(string1.as_str(), string2.as_str());
}
println!("{}", result);
```

---

The borrow checker reasons: `result` needs lifetime `'a`, which must be valid for both `string1` AND `string2`. But `string2` dies at the closing brace, ending `'a`, while `result` is used after that point. Solution: keep `string2` alive until after the `println!`.

