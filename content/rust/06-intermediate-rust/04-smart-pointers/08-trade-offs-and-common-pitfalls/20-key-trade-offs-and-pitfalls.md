## Key Trade-offs and Pitfalls

What are the seven key takeaways about smart pointer trade-offs and pitfalls?

---

**1. Smart pointers have costs**
- Performance: heap allocation, atomic operations
- Complexity: runtime errors, deadlocks

**2. Reference cycles leak memory**
- `Rc` cycles never reach count = 0
- Always use `Weak` for back-references
- Monitor strong/weak counts

**3. RefCell can panic**
- Runtime borrow checking can fail
- Use `try_` methods for safety
- Keep borrows short-lived

**4. Deadlocks are real**
- Inconsistent lock ordering causes deadlocks
- Always lock in same order
- Minimize lock duration

**5. Profile before optimizing**
- Measure, don't guess
- Smart pointer overhead usually acceptable
- Focus on actual bottlenecks

**6. Simpler is better**
- Use regular ownership when possible
- Add smart pointers only when needed
- Start simple, add complexity incrementally

**7. Test concurrency issues**
- Hard to debug in production
- Add stress tests
- Use tools (Valgrind, sanitizers)

**Mental model:**
```
Benefits:
- Shared ownership
- Interior mutability  
- Thread safety

Costs:
- Performance overhead
- Runtime errors (panics, deadlocks)
- Increased complexity
```

**Decision framework:** Use smart pointers when benefits outweigh costs. Always start with simplest solution that works.

