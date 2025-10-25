## Vector Memory Location

Where is a vector's data stored in memory? What about the vector struct itself?

---

The vector's **elements** are stored on the **heap**. The vector struct itself (containing pointer, length, capacity) is stored on the **stack**. This is why vectors can grow dynamically - only the pointer needs to be updated.

