## When to Use su vs sudo

When should a system administrator choose to use su versus sudo?

---

**Use su when:**
- Extended administrative session required
- Multiple root commands need to be executed
- Working in recovery or maintenance mode
- System doesn't have sudo configured
- Need complete root environment

**Use sudo when: (PREFERRED)**
- Single or few administrative commands needed
- Want to maintain audit trail
- Don't want to share root password
- Need granular permission control
- Working on production systems
- Following security best practices

