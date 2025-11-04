## When NOT to Use Rebase

What are three situations where you should NOT use rebase?

---

❌ Don't rebase:
1. On public/shared branches (breaks others' work)
2. After pushing to shared repository (rewrites public history)
3. On commits others have based work on (breaks their branches)

Example of what NOT to do:
```bash
git switch main           # Public branch
git rebase feature        # DANGEROUS!
```

Golden rule: Never rebase public commits. Use merge for shared branches.

