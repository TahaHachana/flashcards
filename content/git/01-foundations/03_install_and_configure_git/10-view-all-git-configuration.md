## View All Git Configuration

What command lists all active Git configuration settings along with the file each comes from?

---

```bash
git config --list --show-origin
```

To list settings without the origin file:
```bash
git config --list
```

To check a single specific value:
```bash
git config user.name
git config user.email
```

