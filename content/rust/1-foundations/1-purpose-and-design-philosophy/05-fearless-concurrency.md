## Fearless Concurrency

What is “fearless concurrency” in Rust and how does the compiler enforce it?

---

It means developers can write concurrent code safely because
Rust’s ownership and type system prevent data races.
Only one mutable reference or multiple immutable references may exist at a time.

```rust
use std::thread;

fn main() {
    let v = vec![1, 2, 3];
    let handle = thread::spawn(move || for x in v { println!("{x}"); });
    handle.join().unwrap();
}
```

Ownership ensures `v` is safely moved into the thread.

