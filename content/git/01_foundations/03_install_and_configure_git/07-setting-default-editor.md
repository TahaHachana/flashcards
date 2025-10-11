## Setting Default Editor

What command sets VS Code as your default Git editor, and when will Git use this editor?

---

`git config --global core.editor "code --wait"`

Git uses this editor for commit messages, interactive rebases, merge conflict resolution, and other operations requiring text input. The `--wait` flag ensures Git waits for you to close the file before continuing.

