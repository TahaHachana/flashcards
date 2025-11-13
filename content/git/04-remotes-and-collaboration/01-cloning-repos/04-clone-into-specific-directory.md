## Clone into Specific Directory

How do you clone a repository into a custom-named directory?

---

Specify directory name after URL:
```bash
git clone <url> <directory-name>
```

Example:
```bash
git clone https://github.com/user/my-project.git custom-name
# Creates 'custom-name' directory instead of 'my-project'
```

Useful when repository name is generic or conflicts with existing directory.

