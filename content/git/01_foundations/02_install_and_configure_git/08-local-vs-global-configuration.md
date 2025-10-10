## Local vs Global Configuration

When would you use local configuration instead of global configuration, and how do you set it?

---

Use local configuration when you need different settings for a specific repository (e.g., work email for work projects, personal email for personal projects).

Example: 
```bash
cd /path/to/specific/repo
git config --local user.email "work@company.com"
```

Local config overrides global config for that repository only.

