## Testing After Resolution

Why must you test after resolving conflicts and what should you test?

---

Conflicts might introduce logical errors even if syntactically correct. Always test:

1. Run test suite:
   ```bash
   npm test
   pytest
   ```

2. Verify functionality:
   - Manual testing of affected features
   - Check integration points

3. Build/compile:
   ```bash
   npm run build
   ```

Merged code might work individually but fail together. Testing catches integration issues.

