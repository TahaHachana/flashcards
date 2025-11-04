## Using Git Merge Tool

How do you use Git's merge tool for resolving conflicts?

---

Configure merge tool:
```bash
# VS Code
git config --global merge.tool vscode
git config --global mergetool.vscode.cmd 'code --wait $MERGED'

# Or vimdiff, meld, etc.
git config --global merge.tool vimdiff
```

Launch during conflict:
```bash
git mergetool
```

Opens configured tool with visual interface for resolving conflicts. Modern IDEs (VS Code, IntelliJ) have built-in conflict resolution UIs.

