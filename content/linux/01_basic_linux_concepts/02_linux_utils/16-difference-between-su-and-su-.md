## Difference Between su and su -

What is the difference between `su root` and `su - root` commands?

---

**`su root`:**
- Switches to root but keeps current user's environment variables
- Working directory remains the same
- Partial switch to root context

**`su - root`** (or `su -l root`):**
- Creates a login shell environment
- Loads root's environment variables and profile
- Changes working directory to `/root`
- Simulates a fresh login as root
- More complete switch (PREFERRED method)

Note: Spaces required on each side of the dash: `su` [space] `-` [space] `root`

