## Three Git Config Levels

What are the three levels of Git configuration, and what is their priority order?

---

```
Level    | Scope              | File Location          | Flag
---------|-------------------|------------------------|----------
System   | All users          | /etc/gitconfig         | --system
Global   | Current user       | ~/.gitconfig           | --global
Local    | Current repo only  | .git/config            | --local
```

**Priority (highest to lowest): Local → Global → System**
Local settings always win over global and system settings.

