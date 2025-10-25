## Safe Detached HEAD Workflow

What's a safe workflow for using detached HEAD for experimentation?

---

1. Enter detached HEAD intentionally:
   ```bash
   git checkout HEAD~5
   ```

2. Make experimental changes and commits

3. Decide what to do:

   Keep work:
   ```bash
   git switch -c experiment-branch
   ```

   Discard work:
   ```bash
   git switch main  # Changes abandoned
   ```

Always make a conscious decision before switching away from detached HEAD.

