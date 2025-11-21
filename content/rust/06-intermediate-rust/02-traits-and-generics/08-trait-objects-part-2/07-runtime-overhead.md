## Runtime Overhead of Dynamic Dispatch

What is the actual runtime cost of dynamic dispatch?

---

Dynamic dispatch typically adds:
- **One pointer dereference** to access vtable (~1-2 nanoseconds)
- **One indirect function call** through function pointer (~1-5 nanoseconds)
- **Potential cache miss** if vtable isn't cached

**Total overhead**: ~2-5 nanoseconds per call

**Perspective**:
- For 1 million calls: 2-5 milliseconds total
- For most applications: completely negligible
- Matters only in: tight loops called millions of times, extremely small methods, hard real-time systems

**Key point**: Don't optimize prematurely! Profile first.

