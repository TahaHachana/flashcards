## Polynomial Simplification Rule

For a polynomial A(n) = aₘnᵐ + aₘ₋₁nᵐ⁻¹ + ... + a₁n + a₀, what is its Big O complexity and why?

---

A(n) = O(nᵐ)

**Why**: Only the **highest-order term** matters in asymptotic analysis. Lower-order terms become negligible as n grows large. The dominant term nᵐ determines the growth rate.

Example: 5n⁴ + 3n² + 7 = O(n⁴) because n⁴ dominates for large n.

