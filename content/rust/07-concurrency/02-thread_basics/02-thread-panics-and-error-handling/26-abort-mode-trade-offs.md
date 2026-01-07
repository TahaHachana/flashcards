## Abort Mode Trade-offs

When should you use panic = 'abort' vs 'unwind'?

---

Use 'abort' when: (1) Binary size matters (embedded, WASM), (2) Performance critical (no unwind overhead), (3) Resources don't need cleanup (OS will reclaim), (4) Panics are truly fatal. Use 'unwind' when: (1) Cleanup is important (close files, release locks), (2) Need to catch panics with catch_unwind, (3) Production services that must not crash, (4) Default case - safer. Most applications should use unwind for robustness.

