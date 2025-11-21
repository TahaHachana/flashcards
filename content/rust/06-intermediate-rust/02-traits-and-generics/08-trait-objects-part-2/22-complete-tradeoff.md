## Complete Trade-off Summary

Summarize all the trade-offs between static and dynamic dispatch.

---

**Static Dispatch (Generics: `<T: Trait>`)**:
- ✅ Zero runtime overhead
- ✅ Can inline methods
- ✅ Full compiler optimizations
- ❌ Larger binary (code bloat)
- ❌ Longer compile times
- ❌ Cannot store different types together
- ❌ Types must be known at compile time

**Dynamic Dispatch (Trait Objects: `&dyn Trait`)**:
- ✅ Smaller binary size
- ✅ Heterogeneous collections
- ✅ Runtime type selection
- ✅ Faster compilation
- ❌ Small runtime cost (~2-5ns per call)
- ❌ Cannot inline
- ❌ Object safety restrictions

**Choose based on**: Performance requirements, binary size constraints, need for heterogeneous collections, and whether types are known at compile time.

**Default**: Start with trait objects, optimize with generics if profiling shows need.

