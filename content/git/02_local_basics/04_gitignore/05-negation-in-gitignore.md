## Negation in .gitignore

How do you use negation in .gitignore to make exceptions, and what's the limitation?

---

Use `!` to negate a pattern (include files that were previously ignored):

```gitignore
*.log              # Ignore all .log files
!important.log     # But don't ignore important.log
```

LIMITATION: Can't un-ignore a file if its parent directory is ignored:
```gitignore
logs/              # Wrong: directory ignored
!logs/important.log  # This won't work

logs/*             # Right: ignore contents
!logs/important.log  # This works
```

Order matters!

