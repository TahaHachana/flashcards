## .gitignore Best Practices

What should always be ignored in .gitignore and what should never be ignored?

---

ALWAYS ignore:

- Dependencies (node_modules/, venv/)
- Build artifacts (dist/, build/, *.class)
- IDE settings (personal, not shared)
- OS files (.DS_Store, Thumbs.db)
- Logs (*.log)
- Sensitive data (.env, API keys)

NEVER ignore:

- Source code
- Configuration templates (.env.example)
- Documentation
- Tests
- Shared project settings

