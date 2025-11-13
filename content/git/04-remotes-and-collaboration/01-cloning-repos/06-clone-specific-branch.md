## Clone Specific Branch

How do you clone a repository and checkout a specific branch?

---

Clone and checkout specific branch:
```bash
git clone -b branch-name <url>
# or
git clone --branch branch-name <url>
```

Example:
```bash
git clone -b develop https://github.com/user/project.git
```

Note: Still clones all branches, just checks out the specified one.

For single branch only: `git clone --single-branch -b branch-name <url>`

