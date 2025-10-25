## Post-Merge Best Practices

What should you do after successfully merging?

---

After merge:
1. Test merged code (run tests, verify functionality)
2. Verify merge: `git log --oneline --graph`
3. Delete feature branch: `git branch -d feature-branch`
4. Push changes (if using remote): `git push origin main`

Checklist:
- [ ] Tests pass
- [ ] History looks correct
- [ ] Feature branch deleted
- [ ] Remote updated

Always test after merging to catch integration issues early.

