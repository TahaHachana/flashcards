## Set Global User Identity

What two commands must you run immediately after installing Git to identify yourself?

---

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

These are written to `~/.gitconfig` and apply to every repository on the machine. This information is embedded in every commit you make as permanent metadata.

