## Array Cache Performance

Why do arrays have excellent cache performance?

---

Arrays have excellent cache performance because of three factors:

1. Spatial locality - Adjacent elements are stored in adjacent memory locations
2. Sequential access is fast - Processor can prefetch next elements automatically
3. Minimal pointer chasing - Direct address calculation without following pointers

When you access array[i], the CPU likely loads array[i+1], array[i+2], etc. into cache automatically.

This makes array traversal much faster in practice than O(n) analysis might suggest, especially compared to pointer-based structures like linked lists.

