## String to &str Conversion - Three Methods

What are three ways to convert a String to &str and what is the performance cost?

---

Three ways:
1. Automatic borrowing: let slice: &str = &s;
2. Explicit full slice: let slice = &s[..];
3. Using as_str method: let slice = s.as_str();

Performance: Zero cost - no allocation, just creates a reference. The original String remains valid.

