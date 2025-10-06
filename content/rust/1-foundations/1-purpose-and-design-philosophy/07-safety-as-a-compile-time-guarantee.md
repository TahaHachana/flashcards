## Safety as a Compile-Time Guarantee

Why is Rust’s approach to safety considered a compile-time guarantee rather than a runtime feature?

---

All memory and concurrency rules are enforced during compilation.
Invalid ownership, borrowing, or thread usage prevents code from compiling,
eliminating entire categories of runtime crashes.

