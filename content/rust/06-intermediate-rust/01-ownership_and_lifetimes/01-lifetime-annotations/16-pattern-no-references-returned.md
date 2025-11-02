## Pattern No References Returned

Do you need to relate lifetimes when a function doesn't return any references?

---

Usually no. When no references are returned, input lifetimes are often independent:
```rust
fn compare<'a, 'b>(x: &'a str, y: &'b str) -> bool {
    x.len() > y.len()
}
```
The function only uses the inputs temporarily, so their lifetimes don't need to be related. (In practice, lifetime elision often makes these annotations unnecessary.)

