## Time vs Space Complexity Trade-off

What is the relationship between time complexity and space complexity? When might you prioritize one over the other?

---

Both measure algorithm efficiency but focus on different resources:
- **Time complexity**: How long algorithm takes
- **Space complexity**: How much memory algorithm uses

**Prioritize time when**: Real-time constraints, user responsiveness critical, memory abundant

**Prioritize space when**: Memory-constrained systems (embedded, mobile), data too large for RAM, multiple concurrent processes

Often there's a **trade-off**: Using more memory (e.g., caching, memoization) can reduce time complexity, while using less memory may increase execution time.

