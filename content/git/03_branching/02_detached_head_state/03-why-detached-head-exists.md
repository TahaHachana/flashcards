## Why Detached HEAD Exists

What are legitimate uses for detached HEAD state?

---

Good uses:
1. Examining old commits (read-only inspection of project history)
2. Testing old versions (reproduce bugs, run tests)
3. Temporary experiments (quick throwaway changes)
4. Bisecting to find bugs (git bisect uses detached HEAD)

Detached HEAD is useful for temporary, read-only work where you don't intend to keep changes.

