## Comparison of su vs sudo

Compare su and sudo across five key security and operational aspects.

---

1. **Password Required:**
   - su: Root password
   - sudo: User's own password

2. **Privilege Level:**
   - su: Complete root access
   - sudo: Specific commands only

3. **Duration:**
   - su: Until `exit` is typed
   - sudo: Single command execution

4. **Auditing:**
   - su: Limited tracking
   - sudo: Comprehensive logging

5. **Accountability:**
   - su: Difficult to track who did what
   - sudo: Full audit trail of all actions

