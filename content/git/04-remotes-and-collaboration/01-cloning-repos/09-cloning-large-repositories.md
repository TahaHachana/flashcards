## Cloning Large Repositories

What are three strategies for cloning large repositories?

---

1. Shallow clone (limited history):
   ```bash
   git clone --depth 1 <url>
   ```

2. Single branch (one branch only):
   ```bash
   git clone --single-branch -b main <url>
   ```

3. Partial clone (commits without large files):
   ```bash
   git clone --filter=blob:none <url>
   ```

Use these to save bandwidth and time. Can get full history later if needed.

