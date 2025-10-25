## UTF-8 Space Efficiency

Why is UTF-8 space-efficient compared to UTF-16 and UTF-32?

---

UTF-8: 1-4 bytes per character
- ASCII: 1 byte (same as pure ASCII)
- Common languages: 2-3 bytes
- Rare characters: 4 bytes

UTF-16: 2-4 bytes per character (wastes space for ASCII)
UTF-32: Always 4 bytes per character (very wasteful)

For most text (especially English and European languages), UTF-8 is significantly smaller.

