## Initialization Order

What is the order of Vim's startup initialization sources?

---

```
1. VIMINIT environment variable (run as an ex command)
2. User vimrc file ($HOME/.vimrc on Unix; _vimrc on Windows)
3. Local .vimrc/.gvimrc/.exrc in the current directory, only if 'exrc' is set
```

