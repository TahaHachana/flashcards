## Basic Clone Command

What happens when you run `git clone <url>`?

---

Git performs these steps:
1. Creates new directory named after repository
2. Initializes `.git` directory inside
3. Downloads all repository data
4. Checks out default branch (usually `main`)
5. Sets up remote connection named `origin`

Example:
```bash
git clone https://github.com/user/project.git
# Creates 'project' directory with full repository
```

