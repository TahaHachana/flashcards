## Compile Time Zero Cost

What is the runtime cost of Rust's data race prevention?

---

Zero runtime cost. All checks happen at compile time through the type system, ownership rules, and Send/Sync traits. There are no runtime checks for thread safety, no garbage collection overhead, and no reference counting (except where explicitly used with Arc). This is "zero-cost abstraction" - you get safety guarantees without paying for them at runtime. The CPU executes the same machine code it would for unsafe concurrent code.

