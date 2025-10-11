## Polynomial vs Exponential Growth

Why are exponential time algorithms (O(2ⁿ), O(3ⁿ)) considered impractical while polynomial algorithms (O(n²), O(n³)) are generally acceptable?

---

**Exponential algorithms** have rapid growth that quickly exceeds any computer's capacity:
- For n=50: O(2ⁿ) takes ~35 years at 1μs per operation
- For n=50: O(3ⁿ) takes ~2000 centuries

**Polynomial algorithms** scale reasonably:
- For n=50: O(n²) takes 25×10⁻⁴ seconds
- For n=50: O(n³) takes 125×10⁻³ seconds

Exponential growth makes algorithms essentially unusable for even moderate input sizes, regardless of hardware improvements.

