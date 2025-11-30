## Default Remote Name Origin

What is "origin" and why is it the default remote name?

---

`origin` is the conventional default name for the primary remote:
- Automatically created when you clone
- Points to repository you cloned from
- Convention, not a requirement (can be renamed)

Instead of typing full URL:
```bash
git push https://github.com/user/project.git main
```

Use nickname:
```bash
git push origin main
```

It's just a convenient shortcut to the remote URL.

