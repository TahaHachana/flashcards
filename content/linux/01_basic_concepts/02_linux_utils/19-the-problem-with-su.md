## The Problem with su

What is the main security limitation of using `su` for privilege escalation, and what issues does this create?

---

**All-or-Nothing Privilege Model:**
- User either has NO administrative privileges (standard user)
- Or has ALL administrative privileges (full root)
- No middle ground for specific tasks

**Issues created:**
- Must share root password with multiple administrators
- Cannot restrict users to specific administrative tasks
- Difficult to audit who performed which actions
- Hard to revoke access (must change root password)
- Cannot delegate specific responsibilities safely

