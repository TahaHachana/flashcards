## Key Principles for Merge Strategies

What are the key principles to remember about fast-forward vs three-way merges?

---

1. Fast-forward: Linear history, no merge commit, target unchanged
2. Three-way: Non-linear, merge commit created, both branches progressed
3. `--no-ff`: Forces merge commit even when fast-forward possible
4. `--ff-only`: Fails if fast-forward not possible
5. Choice depends on team policy, feature complexity, history preferences
6. Visualize with `git log --graph` to understand structure
7. No "better" strategy—each has appropriate use cases

Understanding merge types helps maintain clean, meaningful Git history!

