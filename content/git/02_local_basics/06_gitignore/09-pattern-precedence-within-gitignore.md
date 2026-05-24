## Pattern Precedence Within .gitignore

Given this `.gitignore`, is `src/debug.log` ignored or tracked? Explain the precedence rule.

```gitignore
*.log
!debug.log
*.log
```

---

`src/debug.log` is **ignored**.

Patterns in a `.gitignore` file are evaluated **top to bottom**, and the **last matching pattern wins**. The sequence is:

```
Line 1: *.log        → debug.log is IGNORED
Line 2: !debug.log   → debug.log is UN-IGNORED (negation overrides line 1)
Line 3: *.log        → debug.log is IGNORED again (overrides line 2)
```

The final state is determined by the **last applicable rule**: line 3 wins, so the file is ignored.

This makes placement order important — negation rules must come **after** the rules they intend to override, and nothing should re-match the file afterward.

