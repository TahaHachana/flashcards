## Set Default Editor

How do you configure VS Code as Git's default commit message editor?

---

```bash
git config --global core.editor "code --wait"
```

The `--wait` flag tells Git to pause until the VS Code tab is closed before continuing. Without it, Git would continue immediately, reading an empty message.

Other examples:
```bash
git config --global core.editor "nano"
git config --global core.editor "vim"
```

