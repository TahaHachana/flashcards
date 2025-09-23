## Data Type Gotchas Decision Tree

What are common pitfalls with Rust data types and how do you avoid them?

---

Follow this quick guide:

1. **Integers**
    - Could overflow?  
    - Debug mode → panics.  
    - Release mode → wraps.  
    - Need control? → use `wrapping_*`, `checked_*`, `overflowing_*`, or `saturating_*`.

2. **Floats**
    - Comparing with `==`? → Not reliable.  
    - Use an epsilon check: `(a - b).abs() < f64::EPSILON`.

3. **Strings**
    - Trying `s[0]`? → Not allowed (UTF-8).  
    - Use slicing (`&s[0..1]`) or iteration instead.

4. **Slices**
    - Owner goes out of scope? → Slice becomes invalid.  
    - Keep owner alive for slice lifetime.

5. **Arrays vs Vec**
    - Array size fixed? → Fine.  
    - Need resizing? → Switch to `Vec<T>`.

This tree helps avoid runtime errors and common beginner mistakes.

