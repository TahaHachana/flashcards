## Unwrap Golden Rule

What's the "golden rule" for using `unwrap()` and `expect()` in Rust?

---

**Golden Rule:** 

*"If you're writing `unwrap()` or `expect()`, pause and ask: Could this fail in production? Should I handle this error properly instead?"*

**Follow-up questions:**
- Is this test code? (If yes, it's okay)
- Have I documented why this can't fail?
- Could a user trigger this panic?
- Am I just being lazy about error handling?
- Would `?`, `unwrap_or()`, or `match` be better?

**Remember:**
- `unwrap()`/`expect()` are not error handling - they're giving up
- They convert errors into crashes
- Use them consciously and sparingly
- In production libraries: almost never
- In production applications: only for proven invariants
- In tests: freely

When in doubt, use `?` or proper error handling.

