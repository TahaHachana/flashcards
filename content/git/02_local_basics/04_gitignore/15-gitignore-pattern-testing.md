## .gitignore Pattern Testing

How can you test if your .gitignore patterns work correctly before committing?

---

1. Create test files matching your patterns
2. Run `git status` to see what appears
3. Use `git check-ignore -v` to verify specific files:
   ```bash
   git check-ignore -v test.log
   # Output: .gitignore:3:*.log    test.log
   ```

Test workflow:
```bash
touch test.log test.txt
echo "*.log" > .gitignore
git status  # Only test.txt should appear as untracked
```

Pattern precedence: command-line → .gitignore (same dir) → .gitignore (parent dirs) → .git/info/exclude → global

