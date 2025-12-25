## Rust's Data Race Guarantee

What is Rust's compile-time guarantee regarding data races?

---

If your Rust code compiles, it cannot have data races. Rust prevents data races at compile time through the type system, ownership rules, and Send/Sync traits. This is a unique guarantee - you can still have other concurrency bugs (race conditions, deadlocks), but data races specifically are impossible in safe Rust. The compiler catches them before the program ever runs.

