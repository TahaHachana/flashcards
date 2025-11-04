## Fast-Forward Merge Example Scenario

Walk through a complete fast-forward merge scenario.

---

```bash
# On main at commit A
git switch -c feature/button

# Make commits
git commit -m "B - Add button"
git commit -m "C - Style button"

# Main hasn't changed, switch back
git switch main

# Merge (fast-forward)
git merge feature/button
```

Output: "Fast-forward"

Result:
```
main: A --- B --- C
```

Linear history, main pointer moved from A to C, no merge commit created.

