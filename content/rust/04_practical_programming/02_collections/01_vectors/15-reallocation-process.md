## Reallocation Process

Describe the three steps that happen during vector reallocation.

---

1. Allocate new memory space with double the current capacity
2. Copy all existing elements to the new memory location
3. Free the old memory

This is why frequent reallocations hurt performance.

