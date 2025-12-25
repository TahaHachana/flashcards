## Send Trait Definition

What does the Send trait mean in Rust?

---

Send means a type can be safely transferred (moved) from one thread to another. Ownership can cross thread boundaries. If a type is Send, you can move values of that type into a thread using `thread::spawn(move || ...)`. Most types are Send, including primitives, String, Vec, and Box.

