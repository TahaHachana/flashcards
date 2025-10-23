## Best Practices for Editing /etc Files

What are the best practices for safely editing configuration files in `/etc`?

---

1. **Backup first**: Copy original file (e.g., `cp file file.bak`)
2. **Comment changes**: Document what was changed and why
3. **Test syntax**: Use configuration test commands when available
4. **Version control**: Consider using Git to track changes
5. **Understand before modifying**: Read documentation first
6. **Use proper tools**: Use `visudo` for `/etc/sudoers`
7. **Test thoroughly**: Verify changes work before deploying to production

These practices prevent system breakage and make troubleshooting easier.

