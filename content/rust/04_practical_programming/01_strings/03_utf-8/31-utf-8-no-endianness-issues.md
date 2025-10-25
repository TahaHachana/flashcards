## UTF-8 No Endianness Issues

Why does UTF-8 avoid endianness problems that UTF-16 and UTF-32 have?

---

UTF-8 is byte-oriented, not word-oriented. Each character is a sequence of individual bytes, not multi-byte units that could be arranged in different orders (big-endian vs little-endian). Files can be transferred between systems without conversion or byte-order marks.

UTF-16 and UTF-32 use 16-bit and 32-bit units, which can be stored in different byte orders.

