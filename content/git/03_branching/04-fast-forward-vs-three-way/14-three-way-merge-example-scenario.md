## Three-Way Merge Example Scenario

Walk through a complete three-way merge scenario.

---

```bash
# On main at commit A
git switch -c feature/search
git commit -m "B - Add search"

# Meanwhile, teammate commits to main
git switch main
git pull  # Gets commit C

# Merge feature
git merge feature/search
```

Output: "Merge made by the 'recursive' strategy"

Result:
```
main: A --- C --- M
       \         /
        B ------
```

Merge commit M created with parents C and B, showing parallel development.

