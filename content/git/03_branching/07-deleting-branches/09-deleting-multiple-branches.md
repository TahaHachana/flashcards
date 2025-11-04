## Deleting Multiple Branches

How do you delete multiple branches at once?

---

Multiple specific branches:
```bash
git branch -d feature/login feature/signup feature/profile
```

All merged branches (except main):
```bash
git branch --merged | grep -v '\*\|main\|master' | xargs git branch -d
```

Multiple remote branches:
```bash
git push origin --delete feature/login feature/signup
```

Use carefully—verify branches are truly ready for deletion before bulk operations.

