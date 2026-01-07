## Performance Considerations

Compare the performance implications of: move, clone, and Arc for thread data sharing.

---

Move: zero cost, transfers ownership, data not copied. Clone: copies all data - memory and time cost proportional to data size, creates independent copies. Arc: small cost for atomic operations (increment/decrement reference count), shared access to single copy. Choose: move for single ownership (cheapest), Arc for shared read-only (cheap sharing), clone for independent copies (expensive but necessary). Don't clone large structures if Arc suffices.

