## Shallow Clone

What is a shallow clone and when should you use it?

---

Shallow clone downloads only latest commit (no history):
```bash
git clone --depth 1 <url>
```

Benefits:
- Faster clone
- Smaller download size
- Good for CI/CD or quick testing

Limitations:
- Can't see full history
- Some Git operations limited

Convert to full: `git fetch --unshallow`

Use when you need code quickly but don't need history.

