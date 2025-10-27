## What Is Option<T>?

What is `Option<T>` in Rust and why does it exist instead of using null/nil?

---

`Option<T>` is an enum that represents a value that might or might not exist. It has two variants: `Some(T)` (contains a value) and `None` (no value).

It exists because Rust has no null pointers, which eliminates entire classes of bugs like null pointer exceptions. The compiler forces you to explicitly handle the "nothing" case at compile time, making absence type-safe and explicit.

