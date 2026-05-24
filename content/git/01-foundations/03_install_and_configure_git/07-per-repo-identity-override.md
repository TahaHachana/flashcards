## Per-Repository Identity Override

How do you set a different email address for a specific Git repository (e.g., a work project)?

---

Navigate into the repository, then use `--local` instead of `--global`:

```bash
cd /path/to/work-repo
git config --local user.email "name@company.com"
```

This writes to `.git/config` inside that repo only, overriding the global setting for that project.

