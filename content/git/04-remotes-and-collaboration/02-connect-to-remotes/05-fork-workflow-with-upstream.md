## Fork Workflow with Upstream

How do you set up remotes for a fork workflow?

---

1. Clone YOUR fork:
   ```bash
   git clone https://github.com/your-username/project.git
   ```

2. Add original as upstream:
   ```bash
   git remote add upstream https://github.com/original-owner/project.git
   ```

3. Verify both remotes:
   ```bash
   git remote -v
   # origin    (your fork)
   # upstream  (original repo)
   ```

Now: Push to origin, pull from upstream to stay synced with original.

