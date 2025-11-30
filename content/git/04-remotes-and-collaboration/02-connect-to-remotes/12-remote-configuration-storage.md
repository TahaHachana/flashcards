## Remote Configuration Storage

Where are remote configurations stored?

---

Stored in `.git/config`:

```bash
cat .git/config
```

Example:
```ini
[remote "origin"]
    url = https://github.com/user/project.git
    fetch = +refs/heads/*:refs/remotes/origin/*

[remote "upstream"]
    url = https://github.com/original/project.git
    fetch = +refs/heads/*:refs/remotes/upstream/*
```

Can edit manually or use `git remote` commands. Commands are safer and validate configuration.

