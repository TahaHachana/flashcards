## Panic Abort Mode

What is panic = 'abort' mode, and what are the trade-offs?

---

In abort mode (set in Cargo.toml), panics immediately terminate the process without unwinding. Trade-offs: Benefits - no unwinding overhead, smaller binary size, faster panics. Costs - destructors don't run, resources aren't cleaned up, can't catch panics with catch_unwind. Use when: binary size matters, embedded systems, or when cleanup isn't critical. Default is 'unwind' which provides cleanup guarantees.

