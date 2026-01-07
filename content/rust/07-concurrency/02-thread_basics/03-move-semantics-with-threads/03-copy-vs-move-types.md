## Copy vs Move Types

What's the difference between how Copy and Move types behave with the move keyword in threads?

---

Copy types (i32, bool, &T, etc.) are copied into the thread - the original remains accessible in the parent scope. Move types (String, Vec, types with heap data) are moved - ownership transfers to the thread and the original becomes inaccessible. Example: move || { println!("{}", x) } - if x is i32, it's copied; if x is String, it's moved. This is the same Copy/Move distinction as everywhere else in Rust.

