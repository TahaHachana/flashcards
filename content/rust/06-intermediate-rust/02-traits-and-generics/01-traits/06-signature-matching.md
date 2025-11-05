## Method Signature Matching Rule

What critical rule must you follow when implementing a trait's methods?

---

You MUST match the exact method signature from the trait definition. The parameters and return types must be identical.

If the trait defines `fn compute(&self) -> i32`, you cannot implement it as `fn compute(&self) -> f64` or change the parameters. The compiler will reject signature mismatches.

