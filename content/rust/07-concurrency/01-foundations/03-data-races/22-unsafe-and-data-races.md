## Unsafe and Data Races

Can you have data races in unsafe Rust code?

---

Even in unsafe blocks, raw pointers (*const T, *mut T) are not Send/Sync by default, making it difficult to accidentally create data races. To actually introduce data races, you'd need to: (1) Manually implement Send/Sync using unsafe impl, (2) Then write unsafe code that violates thread safety. This requires multiple intentional steps. Safe Rust cannot have data races - even unsafe code maintains many safety checks unless you explicitly bypass them.

