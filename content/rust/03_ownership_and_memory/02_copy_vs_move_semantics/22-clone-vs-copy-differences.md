## Clone vs Copy Differences

What are the key differences between Clone and Copy?

---

Copy: implicit (automatic), cheap (bit-wise), stack-only types. Clone: explicit (must call .clone()), can be expensive (may allocate heap), works for any type implementing Clone.

