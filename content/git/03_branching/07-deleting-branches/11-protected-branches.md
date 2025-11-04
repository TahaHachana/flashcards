## Protected Branches

Which branches should never be deleted and how are they protected?

---

Never delete:
- `main` / `master` (primary branch)
- `develop` (if using Git Flow)
- `staging` / `production` (deployment branches)
- Release branches (`release/v1.0.0`)

Protection mechanisms:
- GitHub: Branch protection rules
- GitLab: Protected branches
- Bitbucket: Branch permissions

These prevent accidental deletion and require special permissions to modify.

