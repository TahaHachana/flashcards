## Directory-Specific .gitignore

Can you have multiple .gitignore files in a repository and how do they work?

---

Yes! You can place .gitignore files in subdirectories:

```
project/
├── .gitignore       # Applies to entire repo
├── docs/
│   └── .gitignore   # Only applies to docs/ directory
└── src/
    └── .gitignore   # Only applies to src/ directory
```

Patterns in subdirectory .gitignore are relative to that directory. Git checks patterns from specific to general (innermost directory outward).

