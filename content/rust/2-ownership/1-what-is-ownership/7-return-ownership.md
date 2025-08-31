# Return Ownership

How can a function transfer ownership back to its caller?

---

By returning the value, ownership moves to the variable that captures the return.

```rust
fn gives_ownership() -> String {
    String::from("yours")
}

fn takes_and_gives_back(s: String) -> String {
    s
}

let s1 = gives_ownership();            // s1 owns returned String
let s2 = takes_and_gives_back(s1);     // s1 moved into fn and then returned
```