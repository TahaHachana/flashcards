## String Literals Are &str

What type are string literals in Rust and why are they immutable?

---

String literals are &str. They're immutable because they're hardcoded directly into the program binary. The &str points to that location in the executable. Since they're baked into the binary, they cannot be modified at runtime.

