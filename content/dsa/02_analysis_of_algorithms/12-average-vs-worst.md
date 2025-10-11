## When to Use Average vs Worst Case

Under what circumstances should you prefer average case analysis over worst case analysis?

---

**Prefer Average Case when**:
- Input instances are varied and unpredictable
- No prior knowledge of input distribution
- Want measure of typical performance
- Not dealing with real-time constraints

**Prefer Worst Case when**:
- Real-time systems requiring guaranteed response time
- Safety-critical systems
- Need absolute upper bound on performance
- System failure on timeout is unacceptable

