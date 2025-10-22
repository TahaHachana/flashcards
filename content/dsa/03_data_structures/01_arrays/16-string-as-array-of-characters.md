## String as Array of Characters

How are strings represented as arrays, and what is the null character?

---

A string is an array of characters representing text.

Representation:
- Each character occupies one array position
- May end with null character '\0' to mark the end

Example: "HELLO"
[H][E][L][L][O][\0]

Multi-string storage uses a 2D array:
- Each row is one string
- All strings must have same maximum length
- Shorter strings padded with null characters

String operations include: length, concatenation, substring, prefix, suffix.

