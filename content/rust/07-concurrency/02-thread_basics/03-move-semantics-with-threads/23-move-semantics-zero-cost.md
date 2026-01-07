## Move Semantics Zero Cost

What is the runtime cost of move semantics with threads?

---

Zero runtime cost. Move is a compile-time concept that transfers ownership - no runtime operations occur. The data isn't copied or moved in memory (unless it's a Copy type being copied). Move just changes which scope owns the data. The type system tracks ownership at compile time. Arc has runtime cost (atomic operations), but move itself is free. This is zero-cost abstraction - safety without performance penalty.

