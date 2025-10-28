## Unwrap Decision Tree

What's the decision process for determining if you should use `unwrap()` or `expect()`?

---

Ask these questions in order:

1. **Is this test code?** → YES: ✅ Use `unwrap()`/`expect()`
2. **Is this example/prototype?** → YES: ✅ Use `unwrap()` (add TODO)
3. **Can the error occur in production?**
   - NO → Document invariant and use `expect("reason")`
   - YES → Continue...
4. **Can you provide a sensible default?** → YES: Use `unwrap_or()` family
5. **Can you propagate the error?** → YES: Use `?` operator
6. **Is crashing acceptable?** 
   - YES: Use `expect()` with clear message
   - NO: Must handle error properly with `match`/`if let`

**Default answer:** If unsure, use `?` or `match` - they're safer.

