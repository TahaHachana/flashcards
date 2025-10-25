## UTF-8 Core Problem Summary

Summarize the four problems that prevent direct string indexing in Rust.

---

1. Ambiguous meaning: Should s[0] be first byte or first character?
2. Invalid UTF-8: Byte indexing could split multi-byte characters
3. Performance expectations: Users expect O(1), but UTF-8 character access is O(n)
4. Slicing dangers: Arbitrary byte positions could create invalid UTF-8

Solution: Rust requires explicit use of chars() or bytes() to make intentions and costs clear.

