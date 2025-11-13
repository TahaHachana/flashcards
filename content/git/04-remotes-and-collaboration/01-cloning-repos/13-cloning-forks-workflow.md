## Cloning Forks Workflow

What's the proper workflow for cloning a forked repository?

---

1. Fork on GitHub (web interface)
2. Clone YOUR fork:
   ```bash
   git clone git@github.com:your-username/project.git
   ```
3. Add upstream remote:
   ```bash
   git remote add upstream https://github.com/original-owner/project.git
   ```
4. Verify remotes:
   ```bash
   git remote -v
   ```
5. Keep fork updated:
   ```bash
   git fetch upstream
   git merge upstream/main
   git push origin main
   ```

This maintains connection to both your fork and original repository.

