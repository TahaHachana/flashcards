## Key Requirements Traits

What traits must HashMap keys implement and why?

---

Keys must implement:
- `Eq`: For equality comparisons (is this key equal to that key?)
- `Hash`: For hashing (compute storage location)

Most built-in types (integers, strings, etc.) already implement these. Custom types need `#[derive(Eq, Hash)]` or manual implementation.

