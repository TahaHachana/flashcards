## Adding Multiple Remotes

Why and how would you add multiple remotes?

---

Use cases:
- Backup to multiple servers
- Deploy to different platforms
- Sync between services
- Fork workflow (origin + upstream)

Example:
```bash
git remote add github https://github.com/user/project.git
git remote add gitlab https://gitlab.com/user/project.git
git remote add backup git@backup-server.com:project.git
```

Push to specific remote:
```bash
git push github main
git push gitlab main
```

Your repository can connect to unlimited remotes.

