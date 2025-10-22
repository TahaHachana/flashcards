## Polynomial vs Exponential Time

What is the difference between polynomial and exponential time algorithms, and why does it matter?

---

Polynomial time algorithms have complexity O(nᵏ) where k is a constant (e.g., O(n), O(n²), O(n³)). They show manageable growth and are considered efficient.

Exponential time algorithms have complexity O(kⁿ) where k is a constant (e.g., O(2ⁿ), O(3ⁿ)). They show explosive growth and quickly become impractical.

For n=50, a polynomial O(n²) takes milliseconds while exponential O(2ⁿ) takes 35 years. Even fast computers cannot save exponential algorithms for moderately large inputs.

