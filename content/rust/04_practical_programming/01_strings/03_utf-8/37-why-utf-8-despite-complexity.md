## Why UTF-8 Despite Complexity

What are the four major advantages of UTF-8 that justify its indexing complexity?

---

1. Space efficient: ASCII uses 1 byte, common languages 2-3 bytes (smaller than UTF-16/32)
2. Backward compatible: ASCII text is valid UTF-8 with same byte values
3. No endianness issues: Byte-oriented, no byte-order concerns
4. Self-synchronizing: Can find character boundaries from any position

These advantages make UTF-8 the dominant text encoding despite the indexing complexity.

